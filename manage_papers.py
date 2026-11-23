#!/usr/bin/env python
"""Manage the learned-optimizer / metanetwork literature vault.

Subcommands
-----------
  discover  Find new papers in a date window: Semantic Scholar / OpenAlex /
            arXiv keyword search plus forward citations of seed papers (S2 and
            OpenAlex), configured in discovery.toml. Writes a ranked report to
            discovery/ and remembers what it showed so later runs only surface
            unseen papers.
  add       Add papers by arXiv ID / DOI / Semantic Scholar ID / URL to
            papers.bib (metadata from Semantic Scholar, arXiv as fallback).
  enrich    Fill missing abstracts / links / IDs of existing entries and
            upgrade arXiv-only venues once papers get published.
  lint      Report duplicates, missing fields and suspicious entries
            (`--fix` merges duplicates).
  readme    Regenerate README.md (grouped by topic, then year).

Set S2_API_KEY / OPENALEX_API_KEY in the environment for dedicated API quota
(the unauthenticated Semantic Scholar pool is frequently rate-limited; hosts
that keep failing are skipped for the rest of a run).
HTTP responses are cached in .cache/http for 24h (`--no-cache` to bypass).
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import time
import tomllib
import unicodedata
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse

import bibtexparser
import requests
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bwriter import BibTexWriter

ROOT = Path(__file__).resolve().parent
BIB_FILE = ROOT / "papers.bib"
README_FILE = ROOT / "README.md"
BY_YEAR_FILE = ROOT / "BY_YEAR.md"
CONFIG_FILE = ROOT / "discovery.toml"
DISCOVERY_DIR = ROOT / "discovery"
STATE_FILE = DISCOVERY_DIR / "state.json"
LOG_FILE = DISCOVERY_DIR / "LOG.md"
CACHE_DIR = ROOT / ".cache" / "http"

S2_API = "https://api.semanticscholar.org/graph/v1"
ARXIV_API = "https://export.arxiv.org/api/query"
S2_FIELDS = "title,abstract,url,venue,year,publicationDate,authors,externalIds,journal"
S2_INTERVAL = 1.05  # seconds between S2 calls (1 req/s for keyed and shared pools)
ARXIV_INTERVAL = 3.1  # arXiv asks for >= 3s between calls
TODAY = dt.date.today()

ATOM = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom",
        "os": "http://a9.com/-/spec/opensearch/1.1/"}


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def append_log(cmd: str, summary: str) -> None:
    """Append one line to discovery/LOG.md, the running history of vault changes."""
    LOG_FILE.parent.mkdir(exist_ok=True)
    if not LOG_FILE.exists():
        LOG_FILE.write_text("# Vault log\n\nOne line per tool action (newest last).\n\n", "utf-8")
    stamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"- {stamp} `{cmd}` — {summary}\n")


# --------------------------------------------------------------------------- #
# HTTP with throttling, retries and an on-disk cache
# --------------------------------------------------------------------------- #
class Http:
    def __init__(self, use_cache: bool = True, ttl_hours: float = 24):
        self.session = requests.Session()
        self.session.headers["User-Agent"] = "learned-optimizer-vault/2.0 (literature tooling)"
        self.use_cache = use_cache
        self.ttl = ttl_hours * 3600
        self.s2_key = os.environ.get("S2_API_KEY")
        self._last: dict[str, float] = {}
        self._failures: dict[str, int] = {}  # consecutive give-ups per host (circuit breaker)

    def _throttle(self, host: str, interval: float) -> None:
        wait = self._last.get(host, 0.0) + interval - time.monotonic()
        if wait > 0:
            time.sleep(wait)
        self._last[host] = time.monotonic()

    def request(self, method: str, url: str, *, params=None, body=None,
                interval: float = 1.0, parse: str = "json", retries: int = 6):
        key = hashlib.sha256(json.dumps([method, url, params, body], sort_keys=True).encode()).hexdigest()
        cache_path = CACHE_DIR / f"{key}.json"
        if self.use_cache and cache_path.exists() and time.time() - cache_path.stat().st_mtime < self.ttl:
            return json.loads(cache_path.read_text("utf-8"))["body"]

        host = urlparse(url).netloc
        if self._failures.get(host, 0) >= 2:
            return None  # host is persistently throttled/down for this run; skip quickly
        headers = {"x-api-key": self.s2_key} if (self.s2_key and "semanticscholar" in url) else {}
        if "openalex" in url and os.environ.get("OPENALEX_API_KEY"):
            params = {**(params or {}), "api_key": os.environ["OPENALEX_API_KEY"]}
        delay = 3.0
        for _ in range(retries):
            self._throttle(host, interval)
            try:
                r = self.session.request(method, url, params=params, json=body, headers=headers, timeout=90)
            except requests.RequestException as exc:
                status, detail = "network error", str(exc)[:120]
            else:
                if r.status_code == 200:
                    self._failures[host] = 0
                    out = r.json() if parse == "json" else r.text
                    if self.use_cache:
                        CACHE_DIR.mkdir(parents=True, exist_ok=True)
                        cache_path.write_text(json.dumps({"url": url, "body": out}), "utf-8")
                    return out
                if r.status_code == 404:
                    return None
                status, detail = r.status_code, r.text[:160]
                if r.status_code not in (429, 500, 502, 503, 504):
                    log(f"  HTTP {status} for {url}: {detail}")
                    return None
                ra = r.headers.get("Retry-After")
                if ra and ra.isdigit():
                    delay = max(delay, float(ra))
            log(f"  {status} from {host}; retrying in {delay:.0f}s")
            time.sleep(delay)
            delay = min(delay * 2, 60)
        self._failures[host] = self._failures.get(host, 0) + 1
        log(f"  giving up on {url}" + ("  (skipping this host for the rest of the run; "
                                        "set S2_API_KEY / OPENALEX_API_KEY for reliable quota)"
                                        if self._failures[host] >= 2 else ""))
        return None


# --------------------------------------------------------------------------- #
# Identifiers & normalisation
# --------------------------------------------------------------------------- #
ARXIV_RE = re.compile(r"(\d{4}\.\d{4,5}|[a-z\-]+(?:\.[A-Z]{2})?/\d{7})(v\d+)?", re.I)


def clean(text) -> str:
    if not text:
        return ""
    return re.sub(r"\s+", " ", str(text).replace("{", "").replace("}", "")).strip()


def ascii_fold(text: str) -> str:
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()


def norm_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]", "", ascii_fold(clean(title)).lower())


def norm_arxiv(x: str | None) -> str | None:
    if not x:
        return None
    m = ARXIV_RE.search(clean(x))
    return m.group(1).lower() if m else None


def norm_doi(x: str | None) -> str | None:
    if not x:
        return None
    x = clean(x).lower()
    x = re.sub(r"^(https?://)?(dx\.)?doi\.org/", "", x)
    return x or None


def doi_to_arxiv(doi: str | None) -> str | None:
    if doi and doi.startswith("10.48550/arxiv."):
        return norm_arxiv(doi.split("arxiv.", 1)[1])
    return None


def s2_id_from_url(url: str | None) -> str | None:
    m = re.search(r"semanticscholar\.org/paper/(?:[^/]+/)?([0-9a-f]{40})", url or "")
    return m.group(1) if m else None


def identity_keys(*, arxiv=None, doi=None, s2=None, title=None) -> set[str]:
    keys = set()
    arxiv = norm_arxiv(arxiv) or doi_to_arxiv(norm_doi(doi))
    if arxiv:
        keys.add(f"arxiv:{arxiv}")
    if (d := norm_doi(doi)) and not d.startswith("10.48550/arxiv."):
        keys.add(f"doi:{d}")
    if s2:
        keys.add(f"s2:{s2}")
    if title and len(t := norm_title(title)) >= 12:
        keys.add(f"title:{t}")
    return keys


def to_s2_query_id(raw: str) -> str | None:
    """Turn a user-supplied identifier into a Semantic Scholar paper-ID string."""
    raw = raw.strip()
    if re.fullmatch(r"[0-9a-f]{40}", raw):
        return raw
    if raw.upper().startswith(("ARXIV:", "DOI:", "CORPUSID:", "URL:")):
        return raw
    if (s2 := s2_id_from_url(raw)):
        return s2
    if "arxiv.org" in raw or re.fullmatch(ARXIV_RE.pattern, raw, re.I):
        a = norm_arxiv(raw)
        return f"ARXIV:{a}" if a else None
    if (d := norm_doi(raw)) and d.startswith("10."):
        return f"DOI:{d}"
    if raw.startswith("http"):
        return f"URL:{raw}"
    return None


# --------------------------------------------------------------------------- #
# Paper model
# --------------------------------------------------------------------------- #
@dataclass
class Paper:
    title: str
    authors: list[str] = field(default_factory=list)
    year: int | None = None
    date: str | None = None
    venue: str = ""
    abstract: str = ""
    arxiv: str | None = None
    doi: str | None = None
    s2id: str | None = None
    url: str = ""
    category: str | None = None
    sources: set[str] = field(default_factory=set)
    seeds: set[str] = field(default_factory=set)
    queries: set[str] = field(default_factory=set)
    score: float = 0.0
    topic: str | None = None
    seen_before: bool = False

    def keys(self) -> set[str]:
        return identity_keys(arxiv=self.arxiv, doi=self.doi, s2=self.s2id, title=self.title)

    @property
    def ref(self) -> str:
        """Best identifier to pass to `manage_papers.py add`."""
        if self.arxiv:
            return self.arxiv
        if self.doi:
            return self.doi
        return self.s2id or self.url

    @property
    def link(self) -> str:
        return f"https://arxiv.org/abs/{self.arxiv}" if self.arxiv else (self.url or "")

    def merge(self, other: "Paper") -> None:
        for attr in ("year", "date", "arxiv", "doi", "s2id", "category"):
            if not getattr(self, attr) and getattr(other, attr):
                setattr(self, attr, getattr(other, attr))
        for attr in ("venue", "abstract", "url"):
            if len(getattr(other, attr) or "") > len(getattr(self, attr) or ""):
                setattr(self, attr, getattr(other, attr))
        if not self.authors and other.authors:
            self.authors = other.authors
        self.sources |= other.sources
        self.seeds |= other.seeds
        self.queries |= other.queries

    def to_json(self) -> dict:
        d = {k: v for k, v in self.__dict__.items()}
        for k in ("sources", "seeds", "queries"):
            d[k] = sorted(d[k])
        return d


def paper_from_s2(d: dict) -> Paper | None:
    if not d or not d.get("title"):
        return None
    ext = d.get("externalIds") or {}
    venue = d.get("venue") or (d.get("journal") or {}).get("name") or ""
    return Paper(
        title=clean(d["title"]),
        authors=[a.get("name", "") for a in d.get("authors") or [] if a.get("name")],
        year=d.get("year"),
        date=d.get("publicationDate"),
        venue=clean(venue),
        abstract=clean(d.get("abstract")),
        arxiv=norm_arxiv(ext.get("ArXiv")),
        doi=norm_doi(ext.get("DOI")),
        s2id=d.get("paperId"),
        url=d.get("url") or "",
    )


def paper_from_atom(entry: ET.Element) -> Paper:
    def txt(path):
        el = entry.find(path, ATOM)
        return clean(el.text) if el is not None and el.text else ""
    arxiv = norm_arxiv(txt("a:id"))
    published = txt("a:published")[:10]
    cat = entry.find("arxiv:primary_category", ATOM)
    return Paper(
        title=txt("a:title"),
        authors=[clean(a.text) for a in entry.findall("a:author/a:name", ATOM)],
        year=int(published[:4]) if published else None,
        date=published or None,
        venue=txt("arxiv:journal_ref"),
        abstract=txt("a:summary"),
        arxiv=arxiv,
        doi=norm_doi(txt("arxiv:doi")) or None,
        url=f"https://arxiv.org/abs/{arxiv}" if arxiv else "",
        category=cat.get("term") if cat is not None else None,
    )


# --------------------------------------------------------------------------- #
# Source APIs
# --------------------------------------------------------------------------- #
def s2_batch(http: Http, ids: list[str], fields: str = S2_FIELDS) -> list[dict | None]:
    out: list[dict | None] = []
    for i in range(0, len(ids), 400):
        chunk = ids[i:i + 400]
        res = http.request("POST", f"{S2_API}/paper/batch", params={"fields": fields},
                           body={"ids": chunk}, interval=S2_INTERVAL)
        # The batch endpoint returns results in request order, null for unknown IDs.
        out.extend(res if isinstance(res, list) else [None] * len(chunk))
    return out


def s2_title_match(http: Http, title: str) -> dict | None:
    res = http.request("GET", f"{S2_API}/paper/search/match",
                       params={"query": clean(title), "fields": S2_FIELDS}, interval=S2_INTERVAL)
    return (res or {}).get("data", [None])[0] if res else None


def s2_search(http: Http, query: str, since: dt.date, until: dt.date, limit: int) -> list[Paper]:
    papers, offset = [], 0
    while offset < limit:
        res = http.request("GET", f"{S2_API}/paper/search", interval=S2_INTERVAL, params={
            "query": query, "fields": S2_FIELDS, "offset": offset, "limit": min(100, limit - offset),
            "publicationDateOrYear": f"{since.isoformat()}:{until.isoformat()}",
        })
        if not res or not res.get("data"):
            break
        papers += [p for p in map(paper_from_s2, res["data"]) if p]
        if "next" not in res:
            break
        offset = res["next"]
    return papers


def s2_citations(http: Http, paper_id: str, cap: int) -> list[Paper]:
    papers, offset = [], 0
    while offset < cap:
        res = http.request("GET", f"{S2_API}/paper/{paper_id}/citations", interval=S2_INTERVAL,
                           params={"fields": S2_FIELDS, "offset": offset, "limit": 1000})
        if not res or not res.get("data"):
            break
        papers += [p for p in (paper_from_s2(c.get("citingPaper")) for c in res["data"]) if p]
        if "next" not in res:
            break
        offset = res["next"]
    return papers


def arxiv_search(http: Http, query: str, since: dt.date, until: dt.date, cap: int) -> list[Paper]:
    window = f"submittedDate:[{since:%Y%m%d}0000 TO {until:%Y%m%d}2359]"
    papers, start = [], 0
    while start < cap:
        text = http.request("GET", ARXIV_API, interval=ARXIV_INTERVAL, parse="text", params={
            "search_query": f"({query}) AND {window}", "start": start,
            "max_results": min(100, cap - start), "sortBy": "submittedDate", "sortOrder": "descending",
        })
        if not text:
            break
        root = ET.fromstring(text)
        entries = root.findall("a:entry", ATOM)
        papers += [paper_from_atom(e) for e in entries if e.find("a:title", ATOM) is not None]
        total = int(root.findtext("os:totalResults", "0", ATOM))
        start += len(entries)
        if not entries or start >= total:
            break
    return papers


def arxiv_lookup(http: Http, arxiv_ids: list[str]) -> dict[str, Paper]:
    out = {}
    for i in range(0, len(arxiv_ids), 50):
        chunk = arxiv_ids[i:i + 50]
        text = http.request("GET", ARXIV_API, interval=ARXIV_INTERVAL, parse="text",
                            params={"id_list": ",".join(chunk), "max_results": len(chunk)})
        if text:
            for e in ET.fromstring(text).findall("a:entry", ATOM):
                p = paper_from_atom(e)
                if p.arxiv and p.title:
                    out[p.arxiv] = p
    return out


OPENALEX_API = "https://api.openalex.org"
OA_SELECT = ("id,display_name,publication_date,publication_year,authorships,abstract_inverted_index,"
             "ids,doi,primary_location,locations")
OA_INTERVAL = 0.25


def paper_from_openalex(w: dict) -> Paper | None:
    if not w or not w.get("display_name"):
        return None
    inv = w.get("abstract_inverted_index") or {}
    words = sorted(((i, tok) for tok, idx in inv.items() for i in idx))
    ids = w.get("ids") or {}
    arxiv = norm_arxiv(ids.get("arxiv"))
    for loc in w.get("locations") or []:
        if not arxiv and "arxiv.org" in (loc.get("landing_page_url") or ""):
            arxiv = norm_arxiv(loc["landing_page_url"])
    doi = norm_doi(w.get("doi"))
    arxiv = arxiv or doi_to_arxiv(doi)
    src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name") or ""
    return Paper(
        title=clean(w["display_name"]),
        authors=[clean((a.get("author") or {}).get("display_name")) for a in w.get("authorships") or []],
        year=w.get("publication_year"),
        date=w.get("publication_date"),
        venue="" if "arxiv" in src.lower() else clean(src),
        abstract=" ".join(t for _, t in words),
        arxiv=arxiv,
        doi=doi,
        url=f"https://arxiv.org/abs/{arxiv}" if arxiv else (w.get("doi") or w.get("id", "")),
    )


def oa_window(since: dt.date, until: dt.date) -> str:
    # Start at Jan 1 of the start year: OpenAlex stores year-only dates as YYYY-01-01, which
    # would otherwise drop papers. Results are re-filtered precisely by `in_window`.
    return f"from_publication_date:{since.year}-01-01,to_publication_date:{until.isoformat()}"


def oa_search(http: Http, query: str, since: dt.date, until: dt.date, limit: int) -> list[Paper]:
    res = http.request("GET", f"{OPENALEX_API}/works", interval=OA_INTERVAL, params={
        "search": query, "filter": oa_window(since, until), "per-page": min(100, limit), "select": OA_SELECT})
    return [p for p in map(paper_from_openalex, (res or {}).get("results", [])) if p]


def oa_resolve(http: Http, seed_id: str) -> str | None:
    """Resolve an `ARXIV:` / `DOI:` seed id to an OpenAlex work id."""
    kind, _, val = seed_id.partition(":")
    doi = f"10.48550/arxiv.{val}" if kind.upper() == "ARXIV" else val
    res = http.request("GET", f"{OPENALEX_API}/works/doi:{doi.lower()}", interval=OA_INTERVAL,
                       params={"select": "id"})
    return res["id"].rsplit("/", 1)[-1] if res and res.get("id") else None


def oa_lookup(http: Http, query_id: str) -> Paper | None:
    """Fetch one work from OpenAlex given an `ARXIV:` / `DOI:` id."""
    kind, _, val = query_id.partition(":")
    if kind.upper() not in ("ARXIV", "DOI"):
        return None
    doi = f"10.48550/arxiv.{val}" if kind.upper() == "ARXIV" else val
    res = http.request("GET", f"{OPENALEX_API}/works/doi:{doi.lower()}", interval=OA_INTERVAL,
                       params={"select": OA_SELECT})
    return paper_from_openalex(res) if res else None


def oa_citations(http: Http, work_id: str, since: dt.date, until: dt.date, cap: int) -> list[Paper]:
    papers, cursor = [], "*"
    while cursor and len(papers) < cap:
        res = http.request("GET", f"{OPENALEX_API}/works", interval=OA_INTERVAL, params={
            "filter": f"cites:{work_id},{oa_window(since, until)}", "per-page": 200,
            "cursor": cursor, "select": OA_SELECT})
        if not res or not res.get("results"):
            break
        papers += [p for p in map(paper_from_openalex, res["results"]) if p]
        cursor = (res.get("meta") or {}).get("next_cursor")
    return papers


# --------------------------------------------------------------------------- #
# Bib / config / state I/O
# --------------------------------------------------------------------------- #
def load_bib() -> BibDatabase:
    parser = bibtexparser.bparser.BibTexParser(common_strings=True, ignore_nonstandard_types=False)
    with open(BIB_FILE, encoding="utf-8") as f:
        return bibtexparser.load(f, parser=parser)


FIELD_CASE = {"archiveprefix": "archivePrefix", "primaryclass": "primaryClass"}


def save_bib(db: BibDatabase) -> None:
    # bibtexparser lowercases field names on load; restore the conventional casing.
    for e in db.entries:
        for low, cased in FIELD_CASE.items():
            if low in e:
                e.setdefault(cased, e.pop(low))
    writer = BibTexWriter()
    writer.indent = " "
    writer.order_entries_by = ("ID",)
    BIB_FILE.write_text(writer.write(db), encoding="utf-8")


def load_config() -> dict:
    with open(CONFIG_FILE, "rb") as f:
        return tomllib.load(f)


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text("utf-8"))
    return {"runs": [], "seen": {}}


def save_state(state: dict) -> None:
    DISCOVERY_DIR.mkdir(exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", "utf-8")


def entry_keys(e: dict) -> set[str]:
    return identity_keys(arxiv=e.get("arxivid") or e.get("eprint"), doi=e.get("doi"),
                         s2=s2_id_from_url(e.get("url")), title=e.get("title"))


def bib_index(entries: list[dict]) -> set[str]:
    keys: set[str] = set()
    for e in entries:
        keys |= entry_keys(e)
    return keys


def entry_topics(e: dict) -> list[str]:
    return [t.strip() for t in clean(e.get("keywords", "")).split(",") if t.strip()]


STOPWORDS = {"a", "an", "the", "is", "are", "can", "do", "does", "on", "of", "in", "how", "what",
             "why", "when", "to", "for", "and", "with", "from", "by", "this", "we", "our", "should", "be"}


def make_key(p: Paper, taken: set[str]) -> str:
    words = [re.sub(r"[^a-z0-9]", "", ascii_fold(w).lower()) for w in p.title.split()]
    first = next((w for w in words if w and w not in STOPWORDS), "paper")
    last = ascii_fold(p.authors[0].split()[-1]).lower() if p.authors else ""
    base = f"{first}_{re.sub(r'[^a-z]', '', last)}_{p.year or ''}"
    key, n = base, 1
    while key in taken:
        n += 1
        key = f"{base}{chr(ord('a') + n - 1)}"
    return key


def bib_author(name: str) -> str:
    parts = name.split()
    return name if len(parts) < 2 else f"{parts[-1]}, {' '.join(parts[:-1])}"


def paper_to_entry(p: Paper, key: str, topics: list[str]) -> dict:
    e = {"ENTRYTYPE": "article", "ID": key, "title": p.title, "year": str(p.year or "")}
    if p.authors:
        e["author"] = " and ".join(bib_author(a) for a in p.authors)
    if p.abstract:
        e["abstract"] = p.abstract
    e["url"] = p.url or p.link
    if p.arxiv:
        e.update(arxivid=p.arxiv, eprint=p.arxiv, archivePrefix="arXiv", primaryClass=p.category or "cs.LG")
    if p.doi:
        e["doi"] = p.doi
    e["journal"] = p.venue or ("arXiv.org" if p.arxiv else "")
    if p.date:
        e["date"] = p.date
    if topics:
        e["keywords"] = ", ".join(topics)
    e["added"] = TODAY.isoformat()
    return {k: v for k, v in e.items() if v}


# --------------------------------------------------------------------------- #
# discover
# --------------------------------------------------------------------------- #
class Pool:
    """De-duplicating candidate collection keyed by all identity keys."""

    def __init__(self):
        self.by_key: dict[str, Paper] = {}

    def add(self, p: Paper, *, source: str, seed: str | None = None, query: str | None = None):
        p.sources.add(source)
        if seed:
            p.seeds.add(seed)
        if query:
            p.queries.add(query)
        existing = next((self.by_key[k] for k in p.keys() if k in self.by_key), None)
        if existing is not None:
            existing.merge(p)
            p = existing
        for k in p.keys():
            self.by_key[k] = p

    def papers(self) -> list[Paper]:
        return list({id(p): p for p in self.by_key.values()}.values())


def arxiv_month(a: str | None) -> str | None:
    """'2507.01649' -> '2025-07' (new-style arXiv ids encode the submission month)."""
    return f"20{a[:2]}-{a[2:4]}" if a and re.match(r"\d{4}\.\d", a) else None


def in_window(p: Paper, since: dt.date, until: dt.date) -> bool:
    """True if the paper appeared (as preprint or publication) inside the window.

    OpenAlex often stores year-only dates as YYYY-01-01, so for arXiv papers such a
    placeholder date is ignored in favour of the arXiv submission month.
    """
    s, u = since.isoformat(), until.isoformat()
    if (m := arxiv_month(p.arxiv)) and s[:7] <= m <= u[:7]:
        return True
    if p.date:
        if p.date[5:10] == "01-01" and m:
            return False
        return s <= p.date[:10] <= u
    return bool(p.year) and since.year <= p.year <= until.year


def score_paper(p: Paper, cfg: dict) -> None:
    title, text = p.title.lower(), f"{p.title} {p.abstract}".lower()
    rel = cfg.get("relevance", {})
    kw = sum(w for term, w in rel.items() if term in text) + sum(w for term, w in rel.items() if term in title)
    d = cfg["discover"]
    p.score = round(kw + d.get("seed_weight", 1.5) * len(p.seeds) + 0.5 * len(p.queries), 2)
    best, best_hits = None, 0
    for t in cfg.get("topics", []):
        hits = sum(2 if k in title else 1 for k in t.get("keywords", []) if k in text)
        if hits > best_hits:
            best, best_hits = t["id"], hits
    p.topic = best


def cmd_discover(args) -> None:
    cfg, state = load_config(), load_state()
    dcfg = cfg["discover"]
    if args.since:
        since = dt.date.fromisoformat(args.since)
    elif state.get("runs"):
        since = dt.date.fromisoformat(state["runs"][-1]["date"]) - dt.timedelta(days=dcfg.get("overlap_days", 45))
    else:
        since = dt.date.fromisoformat(dcfg["since"])
    until = dt.date.fromisoformat(args.until) if args.until else TODAY
    sources = set(args.sources.split(","))
    http = Http(use_cache=not args.no_cache)
    pool, raw = Pool(), 0
    log(f"Discovery window {since} .. {until}; sources: {', '.join(sorted(sources))}")

    if "s2" in sources:
        for q in cfg["queries"]["s2"]:
            found = s2_search(http, q, since, until, dcfg.get("s2_limit_per_query", 100))
            log(f"[s2-search] {len(found):4d}  {q}")
            raw += len(found)
            for p in found:
                pool.add(p, source="s2-search", query=q)
    if "arxiv" in sources:
        for q in cfg["queries"]["arxiv"]:
            found = arxiv_search(http, q, since, until, dcfg.get("arxiv_max_per_query", 150))
            log(f"[arxiv]     {len(found):4d}  {q}")
            raw += len(found)
            for p in found:
                pool.add(p, source="arxiv", query=q)
    if "citations" in sources:
        for seed in cfg.get("seeds", []):
            found = [p for p in s2_citations(http, seed["id"], dcfg.get("citation_cap_per_seed", 3000))
                     if in_window(p, since, until)]
            log(f"[citations] {len(found):4d}  cite {seed['name']}")
            raw += len(found)
            for p in found:
                pool.add(p, source="citations", seed=seed["name"])
    if "openalex" in sources:
        for q in cfg["queries"].get("openalex", cfg["queries"]["s2"]):
            found = oa_search(http, q, since, until, dcfg.get("s2_limit_per_query", 100))
            log(f"[openalex]  {len(found):4d}  {q}")
            raw += len(found)
            for p in found:
                pool.add(p, source="openalex", query=q)
    if "oa-citations" in sources:
        for seed in cfg.get("seeds", []):
            wid = oa_resolve(http, seed["id"])
            found = oa_citations(http, wid, since, until, dcfg.get("citation_cap_per_seed", 3000)) if wid else []
            log(f"[oa-cites]  {len(found):4d}  cite {seed['name']}" + ("" if wid else "  (seed not in OpenAlex)"))
            raw += len(found)
            for p in found:
                pool.add(p, source="oa-citations", seed=seed["name"])

    entries = load_bib().entries
    known = bib_index(entries)
    seen = state.setdefault("seen", {})
    all_new = [p for p in pool.papers() if not (p.keys() & known) and in_window(p, since, until)]
    for p in all_new:
        score_paper(p, cfg)
        p.seen_before = any(k in seen for k in p.keys())
    all_new.sort(key=lambda p: (-p.score, p.date or ""))
    min_score = args.min_score if args.min_score is not None else dcfg.get("min_score", 4.0)
    shortlist = [p for p in all_new if p.score >= min_score and (args.show_seen or not p.seen_before)]

    DISCOVERY_DIR.mkdir(exist_ok=True)
    stamp = TODAY.isoformat()
    meta = {"date": stamp, "since": since.isoformat(), "until": until.isoformat(),
            "sources": sorted(sources), "raw_results": raw, "unique": len(pool.papers()),
            "not_in_vault": len(all_new), "shortlisted": len(shortlist), "min_score": min_score}
    report = f"candidates_{stamp}_window_{since}_{until}"
    (DISCOVERY_DIR / f"{report}.json").write_text(
        json.dumps({"meta": meta, "candidates": [p.to_json() for p in all_new]}, indent=1, ensure_ascii=False),
        "utf-8")
    (DISCOVERY_DIR / f"{report}.md").write_text(render_report(meta, shortlist), "utf-8")

    if not args.dry_run:
        for p in shortlist:
            for k in p.keys():
                seen.setdefault(k, stamp)
        state.setdefault("runs", []).append(meta)
        save_state(state)
        append_log("discover", f"window {since}..{until}, sources {','.join(sorted(sources))}: "
                               f"{meta['unique']} unique, {len(shortlist)} shortlisted (score>={min_score}) "
                               f"-> discovery/{report}.md")

    log(f"\n{meta['unique']} unique papers, {len(all_new)} not in vault, {len(shortlist)} shortlisted "
        f"(score >= {min_score}). Report: discovery/{report}.md")
    for p in shortlist[:args.top]:
        log(f"  {p.score:5.1f}  {p.date or p.year}  {p.title[:90]}  [{p.ref}]")


def render_report(meta: dict, papers: list[Paper]) -> str:
    out = [f"# Discovery report — {meta['date']}\n",
           f"Window **{meta['since']} → {meta['until']}** · sources: {', '.join(meta['sources'])} · "
           f"{meta['raw_results']} raw hits → {meta['unique']} unique → {meta['not_in_vault']} not in vault → "
           f"**{meta['shortlisted']} shortlisted** (score ≥ {meta['min_score']}, unseen).\n",
           "Add a paper with `python manage_papers.py add --topic <topic> <id>`.\n",
           "| # | Score | Date | Title | Suggested topic | Signals |", "|---|---|---|---|---|---|"]
    for i, p in enumerate(papers, 1):
        sig = []
        if p.seeds:
            sig.append(f"cites {len(p.seeds)} seed(s)")
        if p.queries:
            sig.append(f"{len(p.queries)} query hit(s)")
        title = p.title.replace("|", "\\|")
        out.append(f"| {i} | {p.score:.1f} | {p.date or p.year or ''} | [{title}]({p.link}) | "
                   f"{p.topic or '—'} | {', '.join(sig)} |")
    out.append("\n## Details\n")
    for i, p in enumerate(papers, 1):
        authors = ", ".join(p.authors[:6]) + (" et al." if len(p.authors) > 6 else "")
        out += [f"### {i}. {p.title}",
                f"{authors} · {p.venue or 'preprint'} · {p.date or p.year} · `{p.ref}`  ",
                f"Seeds cited: {', '.join(sorted(p.seeds)) or '—'}  ",
                f"`python manage_papers.py add --topic {p.topic or 'TOPIC'} {p.ref}`\n",
                f"<details><summary>Abstract</summary>\n\n> {p.abstract or 'n/a'}\n</details>\n"]
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------- #
# add
# --------------------------------------------------------------------------- #
def cmd_add(args) -> None:
    cfg = load_config()
    valid_topics = {t["id"] for t in cfg.get("topics", [])}
    topics = [t.strip() for t in (args.topic or "").split(",") if t.strip()]
    if bad := [t for t in topics if t not in valid_topics]:
        sys.exit(f"Unknown topic(s) {bad}; valid: {sorted(valid_topics)}")

    raw_ids = list(args.ids)
    if args.file:
        for line in Path(args.file).read_text("utf-8").splitlines():
            line = line.split("#", 1)[0].strip()
            if line:
                raw_ids.append(line.split()[0])
    qids = []
    for r in raw_ids:
        q = to_s2_query_id(r)
        if not q:
            log(f"Cannot interpret identifier: {r}")
        else:
            qids.append(q)
    if not qids:
        return

    http = Http(use_cache=not args.no_cache)
    db = load_bib()
    known = bib_index(db.entries)
    taken = {e["ID"] for e in db.entries}
    s2_results = [None] * len(qids) if args.skip_s2 else s2_batch(http, qids)
    arxiv_ids = [norm_arxiv(q) for q in qids if q.upper().startswith("ARXIV:")]
    arxiv_ids += [d["externalIds"]["ArXiv"] for d in s2_results if d and (d.get("externalIds") or {}).get("ArXiv")]
    ax = arxiv_lookup(http, sorted({norm_arxiv(a) for a in arxiv_ids if a}))

    cands: dict[str, dict] = {}
    if (reports := sorted(DISCOVERY_DIR.glob("candidates_*.json"), key=lambda f: f.stat().st_mtime)):
        for c in json.loads(reports[-1].read_text("utf-8"))["candidates"]:
            for k in identity_keys(arxiv=c.get("arxiv"), doi=c.get("doi"), s2=c.get("s2id"), title=c.get("title")):
                cands[k] = c

    added, added_keys = 0, []
    for q, d in zip(qids, s2_results):
        p = paper_from_s2(d) if d else None
        a = ax.get(norm_arxiv(q) or "") or (ax.get(p.arxiv) if p and p.arxiv else None)
        if p is None and a is None:
            p = oa_lookup(http, q)  # OpenAlex fallback (DOI-only papers, S2 unavailable)
            if p is None:
                log(f"Not found: {q}")
                continue
        if p is not None and a is not None and not p.s2id:
            p.venue = p.venue or a.venue  # arXiv journal_ref when S2 venue is unavailable
        if p is None:
            p = a
        elif a:
            p.category = a.category
            p.date = p.date or a.date
            p.abstract = p.abstract or a.abstract
        cand = next((cands[k] for k in p.keys() if k in cands), None)
        if cand:  # reuse metadata gathered by the last discovery run (e.g. OpenAlex venue)
            p.venue = p.venue or cand.get("venue") or ""
            p.date = p.date or cand.get("date")
        if p.keys() & known:
            log(f"Already in vault: {p.title}")
            continue
        key = make_key(p, taken)
        entry = paper_to_entry(p, key, topics)
        db.entries.append(entry)
        added_keys.append(key)
        taken.add(key)
        known |= p.keys()
        added += 1
        log(f"+ {key}: {p.title}")

    if added:
        save_bib(db)
        log(f"Added {added} paper(s) to {BIB_FILE.name}.")
        append_log("add", f"+{added} [{','.join(topics) or 'no topic'}]: {', '.join(added_keys)}")
        if not args.no_readme:
            write_views()


# --------------------------------------------------------------------------- #
# enrich
# --------------------------------------------------------------------------- #
def looks_preprint(venue: str) -> bool:
    return not venue or "arxiv" in venue.lower()


def fill_dates(http: Http, entries: list[dict]) -> int:
    """Set `date` (first appearance) from arXiv v1, else from an exact-title OpenAlex match."""
    missing = [e for e in entries if not e.get("date")]
    ax = arxiv_lookup(http, sorted({a for e in missing if (a := norm_arxiv(e.get("arxivid")))}))
    n = 0
    for e in missing:
        a = norm_arxiv(e.get("arxivid"))
        date = ax[a].date if a in ax else None
        if not date:
            res = http.request("GET", f"{OPENALEX_API}/works", interval=OA_INTERVAL, params={
                "search": clean(e.get("title")), "per-page": 5, "select": OA_SELECT})
            for p in filter(None, map(paper_from_openalex, (res or {}).get("results", []))):
                if norm_title(p.title) == norm_title(e.get("title", "")) and p.date and p.date[5:] != "01-01":
                    date = p.date
                    break
        if date:
            e["date"] = date
            n += 1
            log(f"  {e['ID']}: {date}")
        else:
            log(f"  {e['ID']}: no date found")
    return n


def cmd_enrich(args) -> None:
    db = load_bib()
    http = Http(use_cache=not args.no_cache)
    if args.dates:
        if (n := fill_dates(http, db.entries)):
            save_bib(db)
            append_log("enrich --dates", f"filled {n} date(s)")
        if not args.no_readme:
            write_views()
        return
    todo = [e for e in db.entries if args.all or not e.get("abstract") or not e.get("url")
            or (args.venues and looks_preprint(e.get("journal", "")))]
    log(f"{len(todo)} entries to enrich")
    by_id, by_title = {}, []
    for e in todo:
        a = norm_arxiv(e.get("arxivid") or e.get("eprint"))
        s2 = s2_id_from_url(e.get("url"))
        qid = f"ARXIV:{a}" if a else (s2 or (f"DOI:{norm_doi(e['doi'])}" if e.get("doi") else None))
        if qid:
            by_id.setdefault(qid, []).append(e)
        else:
            by_title.append(e)

    results = dict(zip(by_id, s2_batch(http, list(by_id)))) if by_id else {}
    pairs = [(e, results.get(q)) for q, es in by_id.items() for e in es]
    pairs += [(e, s2_title_match(http, e.get("title", ""))) for e in by_title]

    changed = 0
    for e, d in pairs:
        p = paper_from_s2(d) if d else None
        if not p:
            continue
        before = dict(e)
        if not e.get("abstract") and p.abstract:
            e["abstract"] = p.abstract
        if not e.get("url") and p.url:
            e["url"] = p.url
        if p.arxiv and not e.get("arxivid"):
            e.update(arxivid=p.arxiv, eprint=e.get("eprint") or p.arxiv, archivePrefix="arXiv")
            e.setdefault("primaryClass", "cs.LG")
        if p.doi and not e.get("doi"):
            e["doi"] = p.doi
        if args.venues and looks_preprint(e.get("journal", "")) and not looks_preprint(p.venue):
            log(f"  venue: {clean(e.get('title'))[:60]} -> {p.venue}")
            e["journal"] = p.venue
        if e != before:
            changed += 1
    if changed:
        save_bib(db)
        append_log("enrich", f"updated {changed} entr{'y' if changed == 1 else 'ies'}")
    log(f"Updated {changed} entries.")
    if not args.no_readme:
        write_views()


# --------------------------------------------------------------------------- #
# lint
# --------------------------------------------------------------------------- #
def entry_richness(e: dict) -> tuple:
    return (bool(e.get("abstract")), len(clean(e.get("author", "")).split(" and ")), len(e))


def cmd_lint(args) -> None:
    db = load_bib()
    cfg = load_config()
    entries = db.entries
    valid_topics = {t["id"] for t in cfg.get("topics", [])}

    # Union-find over shared identity keys.
    parent = list(range(len(entries)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    def compatible(a: dict, b: dict) -> bool:
        """Title-only matches must not contradict each other's arXiv id or year."""
        xa, xb = norm_arxiv(a.get("arxivid")), norm_arxiv(b.get("arxivid"))
        if xa and xb and xa != xb:
            return False
        ya, yb = clean(a.get("year")), clean(b.get("year"))
        return not (ya.isdigit() and yb.isdigit() and abs(int(ya) - int(yb)) > 1)

    owner: dict[str, int] = {}
    for i, e in enumerate(entries):
        for k in entry_keys(e):
            if k not in owner:
                owner[k] = i
            elif not k.startswith("title:") or compatible(e, entries[owner[k]]):
                parent[find(i)] = find(owner[k])
    groups: dict[int, list[int]] = {}
    for i in range(len(entries)):
        groups.setdefault(find(i), []).append(i)
    dups = [g for g in groups.values() if len(g) > 1]

    problems = 0
    for g in dups:
        problems += 1
        log(f"DUPLICATE: " + " | ".join(f"{entries[i]['ID']}" for i in g) + f"  ({clean(entries[g[0]].get('title'))[:60]})")
    for e in entries:
        tag = e["ID"]
        missing = [f for f in ("abstract", "url", "author", "year") if not e.get(f)]
        if missing:
            problems += 1
            log(f"MISSING {','.join(missing)}: {tag}")
        topics = entry_topics(e)
        if not topics:
            problems += 1
            log(f"NO TOPIC: {tag}")
        elif bad := [t for t in topics if t not in valid_topics]:
            problems += 1
            log(f"UNKNOWN TOPIC {bad}: {tag}")
        a = norm_arxiv(e.get("arxivid"))
        if a and re.match(r"\d{4}\.", a) and e.get("year", "").isdigit():
            ay = 2000 + int(a[:2])
            if abs(ay - int(e["year"])) > 2:
                problems += 1
                log(f"SUSPICIOUS: {tag} year {e['year']} but arXiv {a} is from {ay} — wrong identifier?")

    if args.fix and dups:
        drop = set()
        for g in dups:
            keep = max(g, key=lambda i: entry_richness(entries[i]))
            k = entries[keep]
            for i in g:
                if i == keep:
                    continue
                for f, v in entries[i].items():
                    if f not in k or not k[f]:
                        k[f] = v
                ts = entry_topics(k) + [t for t in entry_topics(entries[i]) if t not in entry_topics(k)]
                if ts:
                    k["keywords"] = ", ".join(ts)
                drop.add(i)
            log(f"merged into {k['ID']}: " + ", ".join(entries[i]["ID"] for i in g if i != keep))
        db.entries = [e for i, e in enumerate(entries) if i not in drop]
        save_bib(db)
        append_log("lint --fix", f"merged {len(drop)} duplicate entr{'y' if len(drop) == 1 else 'ies'}")
        write_views()
    log(f"{problems} issue(s) found in {len(entries)} entries.")


# --------------------------------------------------------------------------- #
# README
# --------------------------------------------------------------------------- #
def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9\- ]", "", text.lower()).replace(" ", "-")


LO_BADGE = "🔗 *LO-linked*"


def is_lo_linked(e: dict) -> bool:
    """Weight-space/metanetwork paper that works on or directly connects to learned optimizers."""
    ts = entry_topics(e)
    return "metanetworks" in ts and "learned-optimizers" in ts


def render_entry(e: dict, extra: str = "") -> str:
    title = clean(e.get("title", "Untitled"))
    url = clean(e.get("url"))
    head = f"[{title}]({url})" if url else title
    if is_lo_linked(e):
        head += f" — {LO_BADGE}"
    meta = [f"**Authors:** {clean(e.get('author', 'Unknown'))}"] + ([extra] if extra else [])
    venue = clean(e.get("journal") or e.get("booktitle"))
    line2 = " · ".join(x for x in [venue and f"*{venue}*", clean(e.get("year"))] if x)
    if (a := norm_arxiv(e.get("arxivid"))):
        line2 += f" · [arXiv:{a}](https://arxiv.org/abs/{a})"
    s = f"### {head}\n" + "  \n".join(meta + [line2]) + "\n\n"
    abstract = clean(e.get("abstract"))
    s += (f"<details>\n<summary>Abstract</summary>\n\n> {abstract}\n</details>\n\n" if abstract
          else "*No abstract available.*\n\n")
    return s + "---\n\n"


def write_readme(entries: list[dict], cfg: dict) -> None:
    state = load_state()
    topics = cfg.get("topics", [])
    order = {t["id"]: i for i, t in enumerate(topics)}
    buckets: dict[str, list[dict]] = {t["id"]: [] for t in topics}
    buckets["uncategorized"] = []
    for e in entries:
        ts = entry_topics(e)
        buckets[ts[0] if ts and ts[0] in order else "uncategorized"].append(e)

    years = sorted({int(e["year"]) for e in entries if clean(e.get("year")).isdigit()})
    runs = state.get("runs", [])
    coverage = max(r["until"] for r in runs) if runs else None  # backfill runs end earlier
    earliest = min(r["since"] for r in runs) if runs else None

    md = ["# Learned Optimizers & Weight-Space Learning — Literature Vault\n",
          f"A curated bibliography of **{len(entries)} papers** on learned optimizers, learning to optimize, "
          "and their connection to graph metanetworks and weight-space learning"
          + (f", spanning {years[0]}–{years[-1]}" if years else "") + ".\n"]
    if coverage:
        md.append(f"Systematic search coverage: **{earliest} → {coverage}** "
                  f"(last discovery run {runs[-1]['date']}; see [discovery/](discovery/)). "
                  "Earlier work comes from the original curated collection.\n")
    md += ["Views: **by topic** (this file) · [by publication year](BY_YEAR.md). "
           f"{LO_BADGE} marks the {sum(is_lo_linked(e) for e in entries)} weight-space / metanetwork papers "
           "that work on or directly connect to learned optimizers.\n",
           "Source of truth: [papers.bib](papers.bib). Both views are generated by "
           "`python manage_papers.py readme` — edit the .bib, not these files.\n",
           "## Contents\n"]
    for t in topics + [{"id": "uncategorized", "title": "Uncategorized"}]:
        if buckets[t["id"]]:
            md.append(f"- [{t['title']}](#{slug(t['title'])}) ({len(buckets[t['id']])})")
    md.append("")
    for t in topics + [{"id": "uncategorized", "title": "Uncategorized", "description": "Needs a topic."}]:
        items = buckets[t["id"]]
        if not items:
            continue
        md.append(f"## {t['title']}\n")
        if t.get("description"):
            md.append(f"_{t['description']}_\n")
        items.sort(key=lambda e: (clean(e.get("date")) or clean(e.get("year")), clean(e.get("title"))), reverse=True)
        md += [render_entry(e) for e in items]
    md.append("## Maintaining this vault\n\n```bash\n"
              "python manage_papers.py discover            # search S2 + arXiv + citations of seeds since last run\n"
              "python manage_papers.py add --topic learned-optimizers 2501.12670   # add by arXiv/DOI/S2 id\n"
              "python manage_papers.py lint [--fix]        # duplicates, missing fields, bad ids\n"
              "python manage_papers.py enrich [--venues]   # fill abstracts/ids, update published venues\n"
              "python manage_papers.py readme              # regenerate this file\n```\n\n"
              "Search queries, seed papers, topics and scoring live in [discovery.toml](discovery.toml).\n")
    README_FILE.write_text("\n".join(md), encoding="utf-8")
    log(f"Wrote {README_FILE.name} ({len(entries)} entries).")


def write_by_year(entries: list[dict], cfg: dict) -> None:
    """Chronological view: grouped by publication year, newest first, by date within a year."""
    titles = {t["id"]: t["title"] for t in cfg.get("topics", [])}
    by_year: dict[str, list[dict]] = {}
    for e in entries:
        by_year.setdefault(clean(e.get("year")) or "Unknown", []).append(e)
    years = sorted(by_year, key=lambda y: (y.isdigit(), y), reverse=True)
    n_link = sum(is_lo_linked(e) for e in entries)
    md = ["# Learned Optimizers & Weight-Space Learning — Papers by Year\n",
          f"All **{len(entries)} papers** of the vault grouped by publication year (newest first) and ordered "
          "by first-appearance date within each year. Topic view: [README.md](README.md).\n",
          f"{LO_BADGE} marks the {n_link} weight-space / metanetwork papers that work on or directly connect "
          "to learned optimizers; other weight-space papers are relevant to that space only.\n",
          "**Years:** " + " · ".join(f"[{y}](#{slug(y)}) ({len(by_year[y])})" for y in years) + "\n"]
    for y in years:
        md.append(f"## {y}\n")
        items = sorted(by_year[y], key=lambda e: (clean(e.get("date")) or f"{y}-00", clean(e.get("title"))),
                       reverse=True)
        for e in items:
            topics = ", ".join(titles.get(t, t) for t in entry_topics(e))
            md.append(render_entry(e, extra=f"**Date:** {clean(e.get('date')) or y} · **Topics:** {topics}"))
    BY_YEAR_FILE.write_text("\n".join(md), encoding="utf-8")
    log(f"Wrote {BY_YEAR_FILE.name} ({len(entries)} entries).")


def write_views() -> None:
    """Regenerate both Markdown views from papers.bib."""
    entries, cfg = load_bib().entries, load_config()
    write_readme(entries, cfg)
    write_by_year(entries, cfg)


def cmd_readme(args) -> None:
    write_views()


# --------------------------------------------------------------------------- #
# Learned-optimizer connection of weight-space papers
# --------------------------------------------------------------------------- #
LO_TERMS = ["learned optimizer", "learned optimization", "learning to optimize", "l2o",
            "meta-learned optimizer", "learned update rule", "velo", "meta-optimizer", "optimizer state"]


def fulltext_counts(http: Http, arxiv_id: str) -> dict | None:
    html = http.request("GET", f"https://arxiv.org/html/{arxiv_id}", interval=ARXIV_INTERVAL, parse="text",
                        retries=3)
    if not html:
        return None
    body, _, refs = html.partition('class="ltx_bibliography')

    def norm(s):
        return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).lower()
    body, refs = norm(body), norm(refs)
    count = lambda text, t: len(re.findall(rf"\b{re.escape(t)}s?\b", text))
    return {"body": {t: c for t in LO_TERMS if (c := count(body, t))},
            "refs": {t: c for t in LO_TERMS if (c := count(refs, t))}}


def cmd_lo_evidence(args) -> None:
    """Full-text evidence of a learned-optimizer connection for weight-space papers."""
    entries = [e for e in load_bib().entries if args.topic in entry_topics(e)]
    http = Http(use_cache=not args.no_cache)
    out = {}
    for e in entries:
        a = norm_arxiv(e.get("arxivid"))
        res = fulltext_counts(http, a) if a else None
        abstract_hits = [t for t in LO_TERMS if re.search(rf"\b{re.escape(t)}", clean(e.get("abstract")).lower())]
        out[e["ID"]] = {"title": clean(e.get("title")), "arxiv": a, "linked": is_lo_linked(e),
                        "abstract": abstract_hits, **(res or {"body": None, "refs": None})}
        r = out[e["ID"]]
        body = sum((r["body"] or {}).values())
        log(f"{'LINK' if r['linked'] else '    '} body={body if r['body'] is not None else '?':>3} "
            f"refs={sum((r['refs'] or {}).values()):>3} abs={len(abstract_hits)}  {e['ID']}")
    path = DISCOVERY_DIR / "lo_evidence.json"
    DISCOVERY_DIR.mkdir(exist_ok=True)
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False), "utf-8")
    log(f"Saved {path.relative_to(ROOT)}. Mark a connected paper by adding `learned-optimizers` to its keywords.")


# --------------------------------------------------------------------------- #
def main() -> None:
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", errors="replace")
    ap =argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("discover", help="find new papers")
    d.add_argument("--since", help="YYYY-MM-DD (default: last run minus overlap, else config)")
    d.add_argument("--until", help="YYYY-MM-DD (default: today)")
    d.add_argument("--sources", default="s2,citations,arxiv,openalex,oa-citations",
                   help="comma-separated subset of: s2, citations (S2), arxiv, openalex, oa-citations")
    d.add_argument("--min-score", type=float)
    d.add_argument("--show-seen", action="store_true", help="include candidates reported in earlier runs")
    d.add_argument("--dry-run", action="store_true", help="do not update discovery/state.json")
    d.add_argument("--top", type=int, default=40, help="how many candidates to print")
    d.add_argument("--no-cache", action="store_true")
    d.set_defaults(func=cmd_discover)

    a = sub.add_parser("add", help="add papers by identifier")
    a.add_argument("ids", nargs="*", help="arXiv id, DOI, S2 id/URL, arxiv URL")
    a.add_argument("--file", help="text file with one identifier per line (# comments allowed)")
    a.add_argument("--topic", help="comma-separated topic ids, primary first")
    a.add_argument("--no-readme", action="store_true")
    a.add_argument("--no-cache", action="store_true")
    a.add_argument("--skip-s2", action="store_true",
                   help="use arXiv/OpenAlex metadata only (when Semantic Scholar is rate-limiting)")
    a.set_defaults(func=cmd_add)

    e = sub.add_parser("enrich", help="fill missing metadata")
    e.add_argument("--all", action="store_true", help="re-check every entry")
    e.add_argument("--venues", action="store_true", help="replace arXiv-only venues with published ones")
    e.add_argument("--dates", action="store_true",
                   help="only fill missing first-appearance dates (arXiv v1 / OpenAlex); no Semantic Scholar")
    e.add_argument("--no-readme", action="store_true")
    e.add_argument("--no-cache", action="store_true")
    e.set_defaults(func=cmd_enrich)

    lt = sub.add_parser("lint", help="check the bib for problems")
    lt.add_argument("--fix", action="store_true", help="merge duplicate entries")
    lt.set_defaults(func=cmd_lint)

    r = sub.add_parser("readme", help="regenerate README.md (by topic) and BY_YEAR.md")
    r.set_defaults(func=cmd_readme)

    lo = sub.add_parser("lo-evidence", help="full-text check of weight-space papers for learned-optimizer content")
    lo.add_argument("--topic", default="metanetworks")
    lo.add_argument("--no-cache", action="store_true")
    lo.set_defaults(func=cmd_lo_evidence)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
