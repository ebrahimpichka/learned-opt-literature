# Learned Optimizers & Weight-Space Learning — Papers by Year

All **113 papers** of the vault grouped by publication year (newest first) and ordered by first-appearance date within each year. Topic view: [README.md](README.md).

🔗 *LO-linked* marks the 6 weight-space / metanetwork papers that work on or directly connect to learned optimizers; other weight-space papers are relevant to that space only.

**Years:** [2026](#2026) (38) · [2025](#2025) (36) · [2024](#2024) (14) · [2023](#2023) (6) · [2022](#2022) (4) · [2021](#2021) (1) · [2020](#2020) (2) · [2018](#2018) (1) · [2017](#2017) (7) · [2016](#2016) (3) · [2001](#2001) (1)

## 2026

### [Learning to Compare Neural Representations from Parameterized Computation Graphs](https://arxiv.org/abs/2611.26081)
**Authors:** Lin, Ya-Wei Eileen and Herbst, Daniel and Jegelka, Stefanie  
**Date:** 2026-11-19 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2026 · [arXiv:2611.26081](https://arxiv.org/abs/2611.26081)

<details>
<summary>Abstract</summary>

> Comparing internal representations across trained models is important for identifying corresponding layers and selecting components for model reuse. Yet, direct comparisons at inference require evaluating candidate models on known reference inputs and collecting their internal activations. In this paper, we study whether internal representation similarity measured across independently trained models can instead be learned to predict in unseen models from their parameterized computations. We introduce a framework that applies a graph metanetwork for mapping each internal site to an embedding derived from its upstream computations while accounting for hidden-coordinate permutation and internal attention-basis transformations. We analyze the structural properties of our estimators and derive conditional guarantees for layer retrieval and stitching candidate selection. Empirically, we find that the learned predictors support relation estimation and low-regret layer retrieval. They also select useful stitching connections while not being trained on stitching outcomes. This opens up a new way to study representation similarity directly from trained neural networks: representational relations learned across a collection of trained models can generalize to new computations, and that the predicted relations can guide candidate selection before direct measurement or adapter fitting for functional evaluations.
</details>

---


### [PDE-State Conditioning for Learned Optimization Using Physics-Informed Neural Networks](https://arxiv.org/abs/2611.25185)
**Authors:** Yasmin, Farzana and Vilalta, Ricardo  
**Date:** 2026-11-18 · **Topics:** Learned Optimizers in Specific Domains  
*arXiv.org* · 2026 · [arXiv:2611.25185](https://arxiv.org/abs/2611.25185)

<details>
<summary>Abstract</summary>

> Physics-informed neural network (PINN) optimization depends on global properties of the underlying PDE and how the physics residual evolves across the domain. Standard optimizers such as Adam use fixed gradient-based statistics, while learned PINN optimizers replace the fixed rule with a learned update built from local parameters and optimization-history features. However, none explicitly use PDE-level information. We study two coupled design questions: what PDE-level information should a learned optimizer observe, and how should that information influence its update? We introduce an 11-dimensional PDE state-capturing operator structure, residual geometry, and short-horizon update response, and use it to condition a structured meta-learned optimizer through bounded feature-wise modulation. Repeated design studies identify the compact residual-geometry state G2 and bounded FiLM as the strongest overall choices among those tested. The resulting PDE-State-conditioned optimizer improves all evaluation metrics (relative-L2, L1, solution MSE, and physics MSE) over Adam and the unconditioned learned optimizer on Linear Advection, KdV, and Burgers.
</details>

---


### [TensorMutation: Learning Weight-Space Mutations of Deep Learning Models on Neural Graphs](https://arxiv.org/abs/2611.09650)
**Authors:** Ahmed, Zaheed and Makedonski, Philip and Grabowski, Jens  
**Date:** 2026-11-06 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2026 · [arXiv:2611.09650](https://arxiv.org/abs/2611.09650)

<details>
<summary>Abstract</summary>

> Mutation testing for deep learning (DL) faces a cost-realism trade-off. The pre-training approach produces realistic but computationally expensive mutants, whereas existing post-training operators modify trained models efficiently but produce mutants that less closely resemble real faults. This study asks whether the trade-off is necessary: can the weight-space effect of a fault-informed pre-training mutation operator be predicted from a trained model, without retraining it? We answer this question with TensorMutation, which represents a trained model as a neural graph and uses a mutation-conditioned graph neural network (GNN) to predict parameter changes. The GNN is trained offline and reused across unseen models so that TensorMutation can generate executable mutants without retraining. We construct a corpus of 25,252 original-mutant pairs from 71 multilayer perceptron (MLP) classifiers using 11 fault-informed pre-training operators, including 25 newly curated subjects. TensorMutation partially reproduces the behavioral effects of pre-training mutations on nine held-out subjects, and direct weight-space supervision significantly improves weight-space fidelity. On 12 real-fault subjects, TensorMutation achieves the highest median behavioral similarity among the evaluated approaches. The improvement over the post-training tool DeepMutation++ is statistically significant (Holm-adjusted p=0.018), whereas the differences from the pre-training tool DeepCrime and the norm-matched random control are not significant. These results show that fault-informed pre-training mutations leave learnable structure in weight space that transfers to unseen models.
</details>

---


### [Learning to Restart: Differentiable Restart Policies for Optimization Dynamics](https://arxiv.org/abs/2611.08883)
**Authors:** Fong, Yiman and Xie, Zhonglin and Wen, Zaiwen  
**Date:** 2026-11-06 · **Topics:** General-Purpose Learned Optimizers  
*arXiv.org* · 2026 · [arXiv:2611.08883](https://arxiv.org/abs/2611.08883)

<details>
<summary>Abstract</summary>

> Adaptive restart mechanisms, which reset the momentum or other auxiliary state of an iterative optimizer, play a central role in the empirical performance of accelerated first-order methods, yet existing restart rules remain almost entirely hand-designed. The obstruction to learning restart policies is that, unlike the typical Learning to Optimize (L2O) setting, the discrete restart events make the resulting trajectory non-differentiable in the algorithm parameters and thus block gradient-based optimization of the restart policy. We resolve this obstruction by developing a differentiable framework for restart policies through their continuous-time limit. We introduce surrogate gradients for the restart events and optimization trajectories that are efficient to compute and provably converge to their continuous-time counterparts. We validate the effectiveness of our surrogate gradients in L2O settings, training restart policies that improve upon standard handcrafted adaptive restart criteria on quadratic and linear programs, and that transfer zero-shot from synthetic quadratics to logistic regression on real datasets.
</details>

---


### [Adapters as Data: The Latent Space of LoRAs](https://arxiv.org/abs/2611.07775)
**Authors:** Grävinghoff, Moritz and Wehmeyer, Konstantin and Asefaw, Aron and Knyazev, Boris and Borth, Damian  
**Date:** 2026-11-05 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2026 · [arXiv:2611.07775](https://arxiv.org/abs/2611.07775)

<details>
<summary>Abstract</summary>

> LoRA adapters are usually treated as finished artifacts rather than as a data modality. Prior work has shown that LoRA adapters populate a low-dimensional manifold that a linear PCA basis already organizes well enough to support different operations such as sampling, editing, and inversion. We ask what a learned, nonlinear latent adds beyond this. We train a transformer autoencoder on the same population of LoRA identity adapters, mapping each into a latent space and compare every operation against the identical operation applied directly to the raw adapter weights. The latent preserves the capabilities already available in weight space, sampling diverse identities and editing individual attributes. Beyond preservation, we show that the latent is far more robust to displacement than weight space, degrading into distorted but still valid faces rather than texture. Fixed-dimensional weight-space representations cannot natively host adapters of more than one rank, so we extend our sequential autoencoder to hold mixed-rank adapters within one shared latent. This gives a path toward treating adapter weights of varying architecture as a single, general modality rather than one tied to a fixed rank, and points to a learned, nonlinear latent as the mechanism that could carry this generalization further, toward heterogeneous populations of adapters.
</details>

---


### [A Night at the LLM Zoo: Data Conditioned Flow Matching for Generating Pretrained LLM Weights](https://arxiv.org/abs/2611.07103)
**Authors:** Biggs, Scott and Soro, Bedionita and Gupta, Saumya and Andreis, Bruno and Hwang, Sung Ju  
**Date:** 2026-11-04 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2026 · [arXiv:2611.07103](https://arxiv.org/abs/2611.07103)

<details>
<summary>Abstract</summary>

> A challenge to Weight Space Learning as it expands from task specific and vision models to Large Language Models (LLMs) is the absence of a well curated and analyzed LLM population. To address this, we train such a model zoo for application to Weight Space Generation by systematically varying the data mixture composition between web text, books, mathematics, coding, and French across populations of 51M, 124M, and 355M parameter GPT-2 Models, each tier with count N = 100. We analyze these populations by cosine similarity, functional diversity, Leave-One-Mixture-Out modeling, and variance decomposition. We show that the zoo contains diverse models whose variation is structured by training mixture composition. We embed the training mixture composition to condition a Flow Matching model of complete pretrained LLM weights in Gram-PCA compressed weight space. By demonstrating zero-shot generalization to held out mixtures, measuring Continuous Ranked Probability Score skill, as well as finding minimal changes in downstream test-set perplexity and general capability benchmark scores, we show that our generator generalizes on the simplex of data mixtures to produce models that perform similarly to those in the zoo ex nihilo. Finally, we produce all source code and artifacts to support the continued expansion of Weight Space Learning and Generation into the LLM domain.
</details>

---


### [Reactive Optimizers](https://arxiv.org/abs/2610.33826)
**Authors:** Bai, Xingjian and Liang, Jia-Hao and Teoh, Jayden and Sitzmann, Vincent  
**Date:** 2026-10-24 · **Topics:** Related Meta-Learning & Hyperparameter Adaptation  
*arXiv.org* · 2026 · [arXiv:2610.33826](https://arxiv.org/abs/2610.33826)

<details>
<summary>Abstract</summary>

> We study a reactive optimizer that uses a pretrained language-model agent to inspect training dynamics and rewrite executable optimizer code during a single training run. The agent can change update rules and schedules for individual parameter groups, without optimizer-specific meta-training or memory transferred from other runs. We evaluate this approach, OPAL, on language modeling and image generation when a recipe has not been tuned for the target setting. Across the evaluated settings, it matches or improves on selected fixed recipes. Analysis of its decisions shows changes to learning-rate schedules, optimizer structure, numerical precision, and momentum. Controlled experiments also show adaptation to repeated data corruption and reduced overfitting. We report these behaviors together with the agent's computational cost and implementation requirements.
</details>

---


### [Bifurcations from Weight Space: JEPAWG on Parametric Dynamical Systems](https://arxiv.org/abs/2610.30847)
**Authors:** Göbel, Tobias and Cheng, Miranda C. N.  
**Date:** 2026-10-22 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2026 · [arXiv:2610.30847](https://arxiv.org/abs/2610.30847)

<details>
<summary>Abstract</summary>

> Trained network weights are increasingly treated as data, but there is rarely ground truth about what a population of models should encode, which hampers systematic validation of weight-space methods. This makes parametric dynamical systems a natural test-bed: the dynamics change qualitatively at submanifolds of parameter space that are, in well-studied families, known analytically or numerically. Fine-tuning a forecasting network at each point of a parameter grid yields a model zoo indexed by a physical parameter, against which weight-space diagnostics can be checked. We build such model zoos for four dynamical systems and analyse them with JEPAWG, a recently proposed joint-embedding hypernetwork built around a learned parameter--weight representation. It was first introduced for neural samplers for lattice field theories, where its latent geometry located the phase transition and estimated the 2D Ising critical exponent. Applied to dynamical systems, JEPAWG is competitive on forecasting with a hypernetwork trained directly for that task, despite being supervised on the parameter--weight correspondence rather than on forecasts. Beyond forecasting, the norm of the parameter-derivative of the decoded weights locates Hopf points and curves, tracks a period-doubling cascade closely enough to give a qualitative estimate of the Feigenbaum constant, and detects a global bifurcation, which has no eigenvalue signature and is therefore invisible to linearisation. As such, JEPAWG provides interpretable insight into the dynamics that is not available from other hypernetworks. Together, these results indicate that JEPAWG is a workable instrument for reading physical structure off a population of trained networks.
</details>

---


### [Interfaces and Modules: A Scalable Representation for Weight-Space Learning across Architectures](https://arxiv.org/abs/2610.21995)
**Authors:** Kozyra, Michał and Bronstein, Michael  
**Date:** 2026-10-15 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2026 · [arXiv:2610.21995](https://arxiv.org/abs/2610.21995)

<details>
<summary>Abstract</summary>

> Weight-space learning across architectures requires representations that respect parameter symmetries and scale to large networks. Existing equivariant tensor encoders require architecture-specific symmetry specifications, while neuron graphs make global attention costly. We introduce a typed graph organized around shared coordinate-permutation actions. Its nodes, called interfaces, represent coordinate spaces whose bound tensor axes must be permuted jointly; operation occurrences, called modules, form typed hyperedges. A compiler derives this graph from supported PyTorch models, with exact recovery of the permutation factors defined by its constraints. The Universal Weight Encoder (UWE) combines local equivariant updates to parameter features with global attention over invariant interface summaries. The small number of interfaces makes global attention practical, and a single encoder processes different supported architectures. UWE is competitive with architecture-specific state-of-the-art methods on established benchmarks. On a new zoo of 1,200 transformers spanning 100 architectures, it outperforms the evaluated baselines at ranking networks within unseen architectures, including architectures larger than those used for training, while using substantially less memory.
</details>

---


### [Graph Metanetworks for Transformer Based Language Models](https://arxiv.org/abs/2610.18471)
**Authors:** Wolanowsky, Yonathan and Bar-Shalom, Guy and Frasca, Fabrizio and Maron, Haggai  
**Date:** 2026-10-13 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2026 · [arXiv:2610.18471](https://arxiv.org/abs/2610.18471)

<details>
<summary>Abstract</summary>

> Weight-space learning treats the weights of neural networks as data, processed by other models called metanetworks. A key challenge is that different weights can realize the same function, related by a group of symmetries the metanetwork should respect. While symmetry-aware metanetworks for simple architectures such as MLPs are well developed, a comprehensive treatment of transformers, and in particular transformer-based language models, is still missing. Importantly, their weight space has a richer symmetry group: beyond neuron permutations, attention introduces continuous general-linear symmetries of the attention matrices and permutations of entire heads. Existing methods for transformer weights either capture only part of these symmetries or are restricted to a single, fixed architecture, and none accounts for language-model-specific components such as the token embeddings. Building on graph metanetworks, we propose a graph-based approach that is both symmetry-aware and applicable across depths and widths. We formalize a weight-space symmetry group of complete decoder-only language models and provide a graph construction that is invariant to it. We further introduce two new transformer-population datasets with novel tasks, such as training-corpus prediction and fine-tuning detection, on which our approach notably outperforms existing baselines.
</details>

---


### [Lightweight and Versatile Learned Optimization by Recombination of Gradient History](https://arxiv.org/abs/2610.09604)
**Authors:** Choi, Minyoung and Maulana, Dalta Imam and Jung, Wanyeong  
**Date:** 2026-10-07 · **Topics:** General-Purpose Learned Optimizers  
*arXiv.org* · 2026 · [arXiv:2610.09604](https://arxiv.org/abs/2610.09604)

<details>
<summary>Abstract</summary>

> This paper presents a lightweight and versatile learned optimizer that dynamically recombines gradient history, represented as averages over disjoint time spans. The optimizer reduces the prediction space to one scalar coefficient per gradient average, shared by multiple parameters. Progressively averaging older gradients minimizes memory cost of long history, while keeping their contributions independently accessible. A 37k-parameter network trained in 0.87 GPU-hours generalizes zero-shot to unseen tasks, lowering validation loss by 9.1% and 0.4% on BERT-Tiny and GPT-Tiny, and improving test accuracy over Adam by 3.5 %p on a Vision Transformer and by 2.7 %p on average across nine graph models, with FLOPs overhead as low as 0.3%.
</details>

---


### [CrossGMN: Graph Metanetworks for Cross-Architecture Weight-Space Transformations](https://arxiv.org/abs/2610.01649)
**Authors:** Dayan, Adir and Eitan, Yam and Maron, Haggai  
**Date:** 2026-10-01 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2026 · [arXiv:2610.01649](https://arxiv.org/abs/2610.01649)

<details>
<summary>Abstract</summary>

> Weight-space networks operate directly on parameters of other neural networks, enabling tasks such as predicting model properties, editing trained models, and generating weights. Weight-space symmetries such as neuron permutations make equivariance a key design principle. However, existing equivariant weight-space architectures have primarily been studied for transformations that preserve the network architecture. In contrast, many practical transformations, including model compression and upscaling, map a trained source network into a target network with a different architecture. In this setting, the source and target permutation symmetries act on different parameter spaces, making equivariance less straightforward to formulate. Our key idea for addressing this mismatch is to reformulate cross-architecture operators with two inputs: a trained source network and an initialization of the target network. This lets us define equivariant cross-architecture operators that refine the initialization of the target network using information from the source network, while being invariant to source-network permutations and equivariant to target-network permutations. Based on this formulation, we introduce CrossGMN, a graph metanetwork that jointly processes both networks through symmetry-preserving cross-network message passing. We prove CrossGMN is universal for continuous cross-architecture operators on compact sets under a general-position assumption. We evaluate CrossGMN for model compression, predicting a smaller network's parameters to accelerate subsequent knowledge distillation. Across 2-D and 3-D INRs and image classification with MLPs, CNNs, and Vision Transformers, CrossGMN speeds up distillation by up to 8.89x, transfers across datasets without retraining (3.78x), and a single model can accelerate compression from heterogeneous source architectures into a common target architecture.
</details>

---


### [Transferable Graph Metanetworks](https://arxiv.org/abs/2610.00420)
**Authors:** Ma, Yuxin and Dayan, Adir and Eitan, Yam and Maron, Haggai and Villar, Soledad  
**Date:** 2026-09-30 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2026 · [arXiv:2610.00420](https://arxiv.org/abs/2610.00420)

<details>
<summary>Abstract</summary>

> A weight space network (or metanetwork) takes the weights of another neural network as input and predicts properties of it. Most prior work trains such models on input networks of one or a few fixed sizes and evaluates them in-distribution. The few attempts at out-of-distribution size generalization remain limited in scope and have achieved only modest success. Consequently, the potential efficiency gains of training on small networks and evaluating on much larger ones remain largely unrealized. We propose Transferable Graph Metanetworks, which extend the graph metanetwork paradigm with a set of modifications that make performance transferable across input networks of different widths. The modifications follow two principles: invariance to the ways in which networks of different widths represent the same function, and continuity, such that weights representing similar functions receive similar predictions. We further study whether size generalization is possible for input networks trained independently from random initialization. Empirically, our modifications significantly improve size generalization on every task we consider. Performance is strongest on input networks trained under the maximal-update parameterization ($μ$P), where it remains robust up to $42\times$ the training width. Theoretically, we explain these observations with infinite-width limit theory: we prove size-generalization guarantees for our model on $μ$P-trained inputs, and explain why it can fail under other parameterizations.
</details>

---


### [SOLAR: A State-Driven Online Learning Rate Scheduler for LLM Pretraining](https://arxiv.org/abs/2609.34681)
**Authors:** Shang, Qiulin and Wang, Binyu and Qiao, Yongqi and Rao, Songde and Wu, Zhoutong and Yuan, Kun  
**Date:** 2026-09-28 · **Topics:** Related Meta-Learning & Hyperparameter Adaptation  
*arXiv.org* · 2026 · [arXiv:2609.34681](https://arxiv.org/abs/2609.34681)

<details>
<summary>Abstract</summary>

> Learning-rate (LR) scheduling plays a central role in large language model (LLM) pretraining, yet current practice still relies heavily on hand-crafted heuristics such as Warmup-Cosine-Decay and Warmup-Stable-Decay. Because these schedules are fixed in advance, they cannot adapt to evolving optimization dynamics. Online learned scheduling within the Learning to Optimize (L2O) framework offers a dynamic alternative, but remains brittle at LLM scale due to noisy signals, delayed feedback, and the risk of catastrophic divergence. We propose SOLAR (State-driven Online Learning rAte scheduleR), a stabilized framework for reliable online LR adaptation. SOLAR uses a base schedule as a reference and learns bounded, state-dependent residual corrections for individual parameter groups. Each correction re-anchors to the base at every step, allowing the policy to adapt the LR without relearning the warmup-decay profile. A lightweight state representation and progress-aware reward guide online learning, while a Circuit-Breaker restores training after rare unsafe actions. Across autoregressive language-model pretraining, SOLAR improves final perplexity over tuned static schedules and automatic LR tuners for dense models from 60M to 1B, AdamW and Muon, and two MoE settings up to 3B. Matched 130M controls show that adding base anchoring and action bounds improves a global PPO controller from 27.09 to 23.74 final PPL, while group-wise control reaches 22.87 on the same two seeds. A residual policy trained on a 60M proxy can also be frozen and reused at larger dense scales without target PPO updates, remaining effective across a fourfold base-LR range. These results establish SOLAR as a practical learned LR controller for LLM pretraining.
</details>

---


### [Finite Probes Suffice: Identifiability and Universality for Weight-Space Learning](https://arxiv.org/abs/2609.33901)
**Authors:** Sarangi, Soutrik and Sverdlov, Yonatan and Dayan, Adir and Maron, Haggai and Dym, Nadav  
**Date:** 2026-09-27 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2026 · [arXiv:2609.33901](https://arxiv.org/abs/2609.33901)

<details>
<summary>Abstract</summary>

> Learning properties of neural networks has recently attracted growing interest, with existing approaches operating either directly on network parameters or through probe-based representations of network behavior. While probing methods have shown strong empirical performance, their theoretical foundations remain limited. In this work, we study when finite probe-based representations are sufficient for learning neural functionals. We establish general identification and universality results for probing, and show that using intermediate hidden representations can provide significantly more informative representations than relying only on final outputs. Motivated by these results, we introduce HIDDENPROBE, a simple architecture for learning from hidden probe responses. Across a range of neural functional benchmarks, including both MLPs and Transformers, HIDDENPROBE consistently improves over existing probing methods and achieves state-of-the-art performance. Our code is publicly available on GitHub.
</details>

---


### [Discovering Symmetries in Neural Network Parameter Spaces](https://arxiv.org/abs/2609.33527)
**Authors:** Zhao, Bo and Dehmamy, Nima and Walters, Robin and Yu, Rose  
**Date:** 2026-09-27 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2026 · [arXiv:2609.33527](https://arxiv.org/abs/2609.33527)

<details>
<summary>Abstract</summary>

> Parameter space symmetries are important for understanding neural networks' loss landscape, training dynamics, and generalization. However, systematically identifying these symmetries remains a challenge. In this paper, we formalize data-dependent parameter symmetries and characterize loss invariance and the group-action axioms through infinitesimal conditions, which provide objectives for jointly learning group generators and nonlinear action maps. Our framework systematically uncovers parameter symmetries, including previously unknown ones. To study larger networks, we establish conditions under which subnetwork symmetries extend to the full model. The same construction gives an explicit family of finite-batch symmetries, providing both analytical examples and a foundation for discovery through small subnetworks. Using the infinitesimal characterization and subnetwork construction, we implement a framework for automated discovery of parameter symmetries, and successfully uncovered symmetries in various architectures, including pretrained transformer models.
</details>

---


### [Permutation-Equivariant Flow Matching for Alignment-Free Neural Weight Generation](https://arxiv.org/abs/2609.32833)
**Authors:** Piven, Arkadi and Eitan, Yam and Bar-Shalom, Guy and Frasca, Fabrizio and Cremers, Daniel and Dagès, Thomas and Kimmel, Ron and Maron, Haggai  
**Date:** 2026-09-26 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2026 · [arXiv:2609.32833](https://arxiv.org/abs/2609.32833)

<details>
<summary>Abstract</summary>

> A trained neural network can be represented by a parameter vector in high dimensions. Learning distributions over these vectors enables the generation of new models across various tasks and architectures. A central challenge is permutation symmetry: permuting hidden neurons can produce distant parameter vectors representing the same function. This introduces variations that a generative model must account for when learning from trained networks. Existing methods typically address this using networks derived from a common base model or costly approximate neuron alignment. We instead parameterize a flow-matching velocity field with a permutation-equivariant Graph Meta Network, enabling direct learning from independently trained networks without alignment. Extensive experiments show that our method closely reproduces the joint statistics of accuracy, functional similarity, and weight similarity of independently trained collections, providing evidence of generation beyond checkpoint memorization. A single conditional model also generates task-specific networks on heterogeneous architectures and generalizes to unseen hidden-width configurations. On a tabular domain-shift task, intermediate conditioning produces individual networks with performance comparable to logit ensembles across both domains. Taken together, our results show how permutation equivariance enables learning from diverse collections of independently trained networks without permutation alignment.
</details>

---


### [Reinforcement learning to choose optimizers](https://arxiv.org/abs/2609.01811)
**Authors:** Schelling, Martin van der and Toshniwal, Deepesh and Bessa, Miguel A.  
**Date:** 2026-09-01 · **Topics:** Related Meta-Learning & Hyperparameter Adaptation  
*arXiv.org* · 2026 · [arXiv:2609.01811](https://arxiv.org/abs/2609.01811)

<details>
<summary>Abstract</summary>

> No single optimization method is uniformly best for all problems, and the most suitable optimizer choice can change during a run. Existing approaches that change optimizer during execution typically predetermine part of the strategy: the portfolio is restricted to one algorithm class, the switch occurs once at a fixed time, or the frequency of decisions is treated as a hyperparameter rather than a learned one. We introduce "Reinforcement Learning to Choose Optimizers", which formulates the optimization algorithm choice as a sequential decision-making problem. At each decision, a recurrent policy reads the current run state and decides both which optimizer should be used next and for how long. The portfolio includes both gradient-based and derivative-free optimizers, and each switch passes on the current best solution and a representative step size. A context proxy conditions a gating network over expert heads, and training employs a decoupled actor-critic whose return is expressed in the same empirical runtime distribution metric used at evaluation. Training tasks and portfolio are designed jointly so that no optimizer dominates. On unseen problems, the learned policy outperforms every portfolio optimizer at all but the smallest budgets, and it remains robust under distribution shift.
</details>

---


### [Weight-Space Mixture-of-Experts for Implicit Neural Representation Classification](https://arxiv.org/abs/2607.29463)
**Authors:** Janik, Stanislaw and Byra, Michal  
**Date:** 2026-07-31 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*Lecture notes in computer science* · 2026 · [arXiv:2607.29463](https://arxiv.org/abs/2607.29463)

<details>
<summary>Abstract</summary>

> Implicit Neural Representations (INRs) encode signals as the weights of a coordinate-based neural network and have recently been proposed as an alternative domain for downstream learning. While promising, classification directly in weight space remains challenging due to the high dimensionality and complex structure of INR parameters. Furthermore, the way discriminative information is distributed across INR weights remains poorly understood. We propose a hierarchical Mixture-of-Experts (HMoE) Transformer that processes INR weights using conditional computation aligned with the structure of the underlying implicit network. Coupled with a meta-learning framework that shapes INR parameters for downstream tasks, our model achieves state-of-the-art accuracy across standard benchmarks, ranging from low-resolution datasets to high-resolution ImageNet-1K. To gain insight into how INRs encode discriminative information, we develop weight-space attribution and pruning methods that identify parameters most relevant for classification. These analyses reveal how class-specific structure emerges within INR layers and support the suitability of MoE architectures for weight-space learning. Our approach advances both the performance and interpretability of weight-space classifiers.
</details>

---


### [FunL2O: LLM-Guided Feature Function Design for Learning to Optimize](https://arxiv.org/abs/2607.27389)
**Authors:** Li, Bingheng and Cai, Junyang and Zhang, Yupeng and Dilkina, Bistra and Kalagnanam, Jayant and Phan, Dzung T.  
**Date:** 2026-07-29 · **Topics:** General-Purpose Learned Optimizers  
*arXiv.org* · 2026 · [arXiv:2607.27389](https://arxiv.org/abs/2607.27389)

<details>
<summary>Abstract</summary>

> Learning-to-optimize (L2O) methods accelerate repeated optimization by training models to predict solutions, warm starts, branching decisions, or other forms of solver guidance. A critical yet largely overlooked component of these pipelines is the feature function that maps problem instances to inputs for machine learning models. Existing L2O methods typically rely on hand-crafted features, making representation design manual and largely fixed across domains. We introduce FunL2O, the first unified framework for automating feature design through LLM-driven program evolution for L2O. In a FunSearch-style loop, an LLM proposes executable feature functions, while a fixed evaluation process retrains the original L2O model and measures downstream optimization performance. We evaluate FunL2O on linear and quadratic programming tasks involving solution prediction and warm-starting, as well as on mixed-integer optimization tasks using GNN-guided backdoor branching and Predict-and-Search. Across continuous and discrete optimization tasks and four LLMs, the evolved features consistently outperform hand-crafted representations. These results establish LLM-driven feature evolution as a general and effective approach to automating representation design in L2O.
</details>

---


### [Efficient Long-Horizon Learning for Learned Optimization](https://arxiv.org/abs/2607.06772)
**Authors:** Huang, Xiaolong and Thérien, Benjamin and Harrison, James and Belilovsky, Eugene  
**Date:** 2026-07-07 · **Topics:** General-Purpose Learned Optimizers  
*arXiv.org* · 2026 · [arXiv:2607.06772](https://arxiv.org/abs/2607.06772)

<details>
<summary>Abstract</summary>

> Learned optimization aims to improve upon hand-designed optimizers (e.g., Adam and Muon) by meta-learning small neural network optimizers over a distribution of tasks. While recent work has greatly advanced the architectural design and inductive biases of learned optimizers (LOs), their meta-training remains biased toward short-unroll learning on particular tasks, resulting in redundant computation and leaving LOs often unable to compete with hand-designed optimizers. We introduce Efficient Long-hOrizon (ELO) learning, an efficient meta-training algorithm that (1) reallocates wasted meta-training compute to longer failure regimes, achieving efficient long-horizon learning, and (2) enforces decoupled progressive expert supervision, providing stable meta-learning signals that additionally improve the generalization of LOs. Our empirical study evaluates ELO for meta-training both element-wise and matrix-based LOs. Across downstream language modeling (GPT-2 and GPT-3 on FineWeb) and image classification (ViT-B/16, ResNet-50 on ImageNet-1K) tasks, ELO substantially improves the long-unroll performance and out-of-distribution generalization of the base LOs. In particular, ELO-Celo2 outperforms well-tuned AdamW and Muon on GPT-2 (30M and 124M) language pretraining. \textitNotably, all ELO baselines require less than 7 H100 GPU-hours for meta-training.
</details>

---


### [WeightCLIP: Aligning Datasets and Models for Weight Space Learning](https://arxiv.org/abs/2607.03551)
**Authors:** Asefaw, Aron and Tzevelekakis, Konstantinos and Falk, Damian and Meynent, Léo and Borth, Damian  
**Date:** 2026-07-03 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2026 · [arXiv:2607.03551](https://arxiv.org/abs/2607.03551)

<details>
<summary>Abstract</summary>

> Weight space learning aims to learn representations of neural network (NN) weights, enabling different downstream tasks. Existing approaches show promising performance, but lacking a way to shape these weight-space representations using information about the datasets the models were trained on, thus limiting downstream applications. We propose WeightCLIP, a method for learning a dataset-aligned latent space for neural networks, where datasets information is induced during training. The NNs are encoded as latent representations using an autoencoder, while dataset samples are encoded using a dataset encoder. The two representations are aligned using a contrastive objective, effectively reshaping the weight-space representations according to the datasets. We demonstrate that such representations can be used for different downstream tasks, including mapping dataset information to a weight-space representation that decode to strong models. In addition, we introduce a latent refinement process for generating models that outperforms standard fine-tuning. Overall, our results demonstrate that explicitly incorporating dataset information improves what can be achieved with weight-space representations across retrieval, generation, and refinement. Code will be available at https://github.com/HSG-AIML/WeightCLIP.
</details>

---


### [Dynamic Neural Graph Encoding of Inference Processes in Deep Weight Space](https://arxiv.org/abs/2607.02166)
**Authors:** Wu, Di and Liu, Huan and Chi, Zhixiang and Yu, Yuanhao and Plataniotis, Konstantinos N. and Wang, Yang  
**Date:** 2026-07-02 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*Transactions on Machine Learning Research, 2026* · 2026 · [arXiv:2607.02166](https://arxiv.org/abs/2607.02166)

<details>
<summary>Abstract</summary>

> The rapid advancements in using neural networks as implicit data representations have attracted significant interest in developing machine learning methods that analyze and process the weight spaces of other neural networks. However, efficiently handling these highdimensional weight spaces remains challenging. Existing methods often overlook the sequential nature of layer-by-layer processing in neural network inference. In this work, we propose a novel approach using dynamic graphs to represent neural network parameters, capturing the temporal dynamics of inference. Our Dynamic Neural Graph Encoder (DNG-Encoder) processes these graphs, preserving the sequential nature of neural processing. Additionally, we also leverage DNG-Encoder to develop INR2JLS (Implicit Neural Representation to Joint Latent Space) for facilitate downstream applications, such as classifying Implicit Neural Representations (INRs). Our approach demonstrates significant improvements across multiple tasks, surpassing the state-of-the-art INR classification accuracy by approximately 10% on the CIFAR-100-INR.
</details>

---


### [Exploiting weight-space symmetries for approximating curvature](https://arxiv.org/abs/2606.00442)
**Authors:** Artemev, Artem and Xia, Rui and Boyd, Benjamin M. and Yu, Youjing and Dangel, Felix and Hennequin, Guillaume and Bernacchia, Alberto  
**Date:** 2026-05-30 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2026 · [arXiv:2606.00442](https://arxiv.org/abs/2606.00442)

<details>
<summary>Abstract</summary>

> Many machine learning techniques rely on approximating a loss function's curvature, but this is notoriously hard to do at the scale of modern deep networks. Surprisingly, no previous work has exploited the curvature constraints that arise from well known weight-space symmetries in loss landscapes. By analytically averaging over group actions that leave the loss invariant, we construct structured Hessian approximations from single gradients that can be tractably estimated, stored, and inverted. The choice of user-specified symmetry group directly governs the trade-off between approximation accuracy and computational cost. Moreover, our framework provides a unifying theoretical lens for viewing existing methods; in particular, a specific choice of symmetry group recovers Shampoo/Muon-like curvature estimates. We validate our method on a range of network architectures, and deploy it to second-order optimization benchmarks, including a small language model. Our curvature estimation framework might find applications in other machine learning problems such as uncertainty estimation, continual learning, compression/pruning, training data attribution, and more.
</details>

---


### [What Linear Probes Miss: Multi-View Probing for Weight-Space Learning](https://arxiv.org/abs/2605.23410)
**Authors:** Heo, Eunwoo and Seo, Kyeongkook and Yoo, Jaejun  
**Date:** 2026-05-22 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2026 · [arXiv:2605.23410](https://arxiv.org/abs/2605.23410)

<details>
<summary>Abstract</summary>

> The explosive growth of open-source model repositories has created a Model Jungle, where checkpoints are frequently shared without adequate documentation or metadata. While weight-space learning offers a pathway to identify and analyze these models directly from their parameters, processing full-scale weights is computationally prohibitive. Probing-based methods have emerged as a lightweight alternative, extracting permutation-equivariant representations via learnable probe vectors. However, existing probing methods are limited by a single-view design: they capture first-order structures but fail to encode the rich, higher-order correlation patterns inherent in row-column interactions. To bridge this gap, we introduce MVProbe, a multi-perspective probing framework that synthesizes first-order signals with interaction-aware (Gram-based) views. Our approach is theoretically grounded; we analyze the scaling laws of different probing orders to derive a principled standardization and fusion strategy that ensures balanced contributions from all branches. On the Model Jungle benchmark, MVProbe consistently outperforms the state-of-the-art ProbeX across diverse architectures, including discriminative backbones (ResNet, SupViT, MAE, DINO) and large-scale generative LoRA adapters (Stable Diffusion LoRA).
</details>

---


### [Position: Weight Space Should Be a First-Class Generative AI Modality](https://arxiv.org/abs/2605.18632)
**Authors:** Wang, Zhangyang and Wang, Peihao and Wang, Kai  
**Date:** 2026-05-18 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2026 · [arXiv:2605.18632](https://arxiv.org/abs/2605.18632)

<details>
<summary>Abstract</summary>

> Neural network checkpoints have quietly become a large-scale data resource: millions of trained weight vectors now exist, each encoding task-, domain-, and architecture-specific knowledge. This position paper argues that model checkpoints should be treated as a first-class data modality, and that generative modeling in weight space should be standardized as a core machine learning primitive. Recent advances demonstrate that neural weights can be synthesized on demand, often matching fine-tuning performance while reducing adaptation cost by orders of magnitude. We contend that these results reflect an underlying structural fact: high-performing models occupy low-dimensional, highly structured regions of weight space shaped by symmetry, flatness, modularity, and shared subspaces. Building on this view, we organize existing methods into a five-stage pipeline, survey applications where the approach is already practical, and clarify current limits: adapter-scale and conditional generation are advancing rapidly, while unrestricted frontier-scale checkpoint synthesis remains open. Our goal is to shift the community's default mindset from optimizing models per task to sampling models from learned weight distributions, accelerating toward an era in which AI systems routinely improve or create other AI systems.
</details>

---


### [Learn2Splat: Extending the Horizon of Learned 3DGS Optimization](https://arxiv.org/abs/2605.15760)
**Authors:** Pearl, Naama and Esposito, Stefano and Xu, Haofei and Peleg, Amit and Gschossmann, Patricia and Porzi, Lorenzo and Kontschieder, Peter and Pons-Moll, Gerard and Geiger, Andreas  
**Date:** 2026-05-15 · **Topics:** Learned Optimizers in Specific Domains  
*arXiv.org* · 2026 · [arXiv:2605.15760](https://arxiv.org/abs/2605.15760)

<details>
<summary>Abstract</summary>

> 3D Gaussian Splatting (3DGS) optimization is most commonly performed using general-purpose first-order optimizers such as Adam or SGD. Although robust across scenes, they update each parameter independently without exploiting the structural and spatial relationships among Gaussians, which slows convergence. Recent works introduced learned optimizers that predict correlated updates informed by inter-parameter and inter-Gaussian dependencies. However, those are trained for a fixed number of optimization iterations and rely on manually scheduled learning rates to avoid degradation. In this paper, we introduce Learn2Splat, a learned optimizer for 3DGS that avoids degradation over extended optimization horizons without auxiliary mechanisms. To enable this, we propose a meta-learning scheme that extends the optimization horizon via a checkpoint buffer and an optimizer rollout strategy, combined with an architecture that encodes gradient scale information in its latent states. Results show higher novel view synthesis quality at equal wall-clock time, while remaining stable over long horizons, with zero-shot generalization to unseen datasets and settings. To support our findings, we build a unified framework to train and evaluate learned and standard optimizers across sparse and dense view settings. Code and models will be released publicly. Our project page is available at https://autonomousvision.github.io/learn2splat .
</details>

---


### [Is Class Signal Clustered or Routed in Task-Induced Implicit Neural Representation Weight Spaces?](https://arxiv.org/abs/2605.08281)
**Authors:** Guo, Xinyi and He, Mingyi and Ding, Haobin and Chen, Weiming and Chen, Xinrui and Li, Jiawen and Zhang, Di and Ouyang, Minxi and Wang, Yizhi and Ling, Xitong  
**Date:** 2026-05-08 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2026 · [arXiv:2605.08281](https://arxiv.org/abs/2605.08281)

<details>
<summary>Abstract</summary>

> Implicit neural representations (INRs) encode images as neural-network weights, making image classification a problem of weight-space classifiability. A natural geometric hypothesis is that classifier feedback should make image-specific weights cluster by class in the shared-anchor coordinate. We test this hypothesis in the SIREN-based Meta Weight Transformer (MWT) regime, where end-to-end training meta-learns a shared initialization and inner-loop update schedule for fitting image-specific SIRENs. We find that this prediction fails. Exposed weight-space geometry and supervised clustering pressure do not reliably track trained-reader accuracy; clustering can even make local neighborhoods more class-consistent while making the trained reader worse. Crucially, the reader constructs rather than inherits class-aligned geometry: token-flow diagnostics show that class-aligned neighborhoods become strongly predictive of trained-reader accuracy only after late reader interactions, not in the input coordinate. We further identify the native SIREN bias column in the augmented weight token as a low-dimensional, sample-dependent causal readout route for the trained reader; targeted controls rule out generic scalar-column and marginal-distribution artifacts. The diagnosis motivates interventions that strengthen reader routing, add an explicit bias route, or use denser inner-loop fitting; under the lane-specific training conventions used here, route-directed variants often outperform the shared-anchor baseline but interact non-additively. Task-induced INR weights are classifiable not because they form raw geometric clusters, but because their class signal is routed through the reader.
</details>

---


### [Quasi-Equivariant Metanetworks](https://arxiv.org/abs/2604.23720)
**Authors:** Tran, Viet-Hoang and Nguyen, An and Guérand, Benoît and Vo, Thieu N. and Nguyen, Tan M.  
**Date:** 2026-04-26 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*International Conference on Learning Representations* · 2026 · [arXiv:2604.23720](https://arxiv.org/abs/2604.23720)

<details>
<summary>Abstract</summary>

> Metanetworks are neural architectures designed to operate directly on pretrained weights to perform downstream tasks. However, the parameter space serves only as a proxy for the underlying function class, and the parameter-function mapping is inherently non-injective: distinct parameter configurations may yield identical input-output behaviors. As a result, metanetworks that rely solely on raw parameters risk overlooking the intrinsic symmetries of the architecture. Reasoning about functional identity is therefore essential for effective metanetwork design, motivating the development of equivariant metanetworks, which incorporate equivariance principles to respect architectural symmetries. Existing approaches, however, typically enforce strict equivariance, which imposes rigid constraints and often leads to sparse and less expressive models. To address this limitation, we introduce the novel concept of quasi-equivariance, which allows metanetworks to move beyond the rigidity of strict equivariance while still preserving functional identity. We lay down a principled basis for this framework and demonstrate its broad applicability across diverse neural architectures, including feedforward, convolutional, and transformer networks. Through empirical evaluation, we show that quasi-equivariant metanetworks achieve good trade-offs between symmetry preservation and representational expressivity. These findings advance the theoretical understanding of weight-space learning and provide a principled foundation for the design of more expressive and functionally robust metanetworks.
</details>

---


### [W2T: LoRA Weights Already Know What They Can Do](https://arxiv.org/abs/2603.15990)
**Authors:** Han, Xiaolong and Neri, Ferrante and Jiang, Zijian and Wu, Fang and Ye, Yanfang and Yin, Lu and Wang, Zehong  
**Date:** 2026-03-16 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*Conference on Empirical Methods in Natural Language Processing (EMNLP)* · 2026 · [arXiv:2603.15990](https://arxiv.org/abs/2603.15990)

<details>
<summary>Abstract</summary>

> Each LoRA checkpoint compactly stores task-specific updates in low-rank weight matrices, offering an efficient way to adapt large language models to new tasks and domains. In principle, these weights already encode what the adapter does and how well it performs. In this paper, we ask whether this information can be read directly from the weights, without running the base model or accessing training data. A key obstacle is that a single LoRA update can be factorized in infinitely many ways. Without resolving this ambiguity, models trained on the factors may fit the particular factorization rather than the underlying update. To this end, we propose \methodfull, which maps each LoRA update to a provably canonical form via QR decomposition followed by SVD, so that all equivalent factorizations share the same representation. The resulting components are then tokenized and processed by a Transformer to produce a weight-space embedding. Across language and vision LoRA collections, W2T achieves strong results on attribute classification, performance prediction, and adapter retrieval, demonstrating that LoRA weights reliably indicate model behavior once factorization ambiguity is removed. Code is available at https://github.com/xiaolonghan2000/Weight2Token.
</details>

---


### [A Survey of Weight Space Learning: Understanding, Representation, and Generation](https://arxiv.org/abs/2603.10090)
**Authors:** Han, Xiaolong and Wang, Zehong and Zhao, Bo and Zhang, Binchi and Li, Jundong and Borth, Damian and Yu, Rose and Maron, Haggai and Ye, Yanfang and Yin, Lu and Neri, Ferrante  
**Date:** 2026-03-10 · **Topics:** Surveys, Tutorials & Benchmarks, Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2026 · [arXiv:2603.10090](https://arxiv.org/abs/2603.10090)

<details>
<summary>Abstract</summary>

> Neural network weights are typically viewed as the end product of training, while most deep learning research focuses on data, features, and architectures. However, recent advances show that the set of all possible weight values (weight space) itself contains rich structure: pretrained models form organized distributions, exhibit symmetries, and can be embedded, compared, or even generated. Understanding such structures has tremendous impact on how neural networks are analyzed and compared, and on how knowledge is transferred across models, beyond individual training instances. This emerging research direction, which we refer to as Weight Space Learning (WSL), treats neural weights as a meaningful domain for analysis and modeling. This survey provides the first unified taxonomy of WSL. We categorize existing methods into three core dimensions: Weight Space Understanding (WSU), which studies the geometry and symmetries of weights; Weight Space Representation (WSR), which learns embeddings over model weights; and Weight Space Generation (WSG), which synthesizes new weights through hypernetworks or generative models. We further show how these developments enable practical applications, including model retrieval, continual and federated learning, neural architecture search, and data-free reconstruction. By consolidating fragmented progress under a coherent framework, this survey highlights weight space as a learnable, structured domain with growing impact across model analysis, transferring, and weight generation. We release an accompanying resource at https://github.com/Zehong-Wang/Awesome-Weight-Space-Learning.
</details>

---


### [NNiT: Width-Agnostic Neural Network Generation with Structurally Aligned Weight Spaces](https://arxiv.org/abs/2603.00180)
**Authors:** Kim, Jiwoo and Mehta, Swarajh and Hsu, Hao-Lun and Ryu, Hyunwoo and Liu, Yudong and Pajic, Miroslav  
**Date:** 2026-02-26 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2026 · [arXiv:2603.00180](https://arxiv.org/abs/2603.00180)

<details>
<summary>Abstract</summary>

> Generative modeling of neural network parameters is often tied to architectures because standard parameter representations rely on known weight-matrix dimensions. Generation is further complicated by permutation symmetries that allow networks to model similar input-output functions while having widely different, unaligned parameterizations. In this work, we introduce Neural Network Diffusion Transformers (NNiTs), which generate weights in a width-agnostic manner by tokenizing weight matrices into patches and modeling them as locally structured fields. We establish that Graph HyperNetworks (GHNs) with a convolutional neural network (CNN) decoder structurally align the weight space, creating the local correlation necessary for patch-based processing. Focusing on Multilayer Perceptrons (MLPs), where permutation symmetry is especially apparent, NNiTs generate fully functional networks across a range of architectures. Our approach jointly models discrete architecture tokens and continuous weight patches within a single sequence model. On ManiSkill3 robotics tasks, NNiT achieves $>85\%$ success on architecture topologies unseen during training, while baseline approaches fail to generalize; the same pipeline also generalizes to MNIST classification beyond the robotic control setting.
</details>

---


### [Celo2: Towards Learned Optimization Free Lunch](https://arxiv.org/abs/2602.19142)
**Authors:** Moudgil, Abhinav and Knyazev, Boris and Belilovsky, Eugene  
**Date:** 2026-02-22 · **Topics:** General-Purpose Learned Optimizers  
*International Conference on Learning Representations* · 2026 · [arXiv:2602.19142](https://arxiv.org/abs/2602.19142)

<details>
<summary>Abstract</summary>

> Learned optimizers are powerful alternatives to hand-designed update rules like Adam, yet they have seen limited practical adoption since they often fail to meta-generalize beyond their training distribution and incur high meta-training cost. For instance, prior work, VeLO, scaled meta-training to 4,000 TPU months ($\sim$10$\times$ GPT-3 compute) to meta-train a general-purpose optimizer but it failed to generalize beyond 600M parameters tasks. In this work, we present a surprising finding: by crafting a simple normalized optimizer architecture and augmenting meta-training, it becomes feasible to meta-train a performant general-purpose learned update rule on a tiny fraction of VeLO compute, 4.5 GPU hours to be precise. Our learned update rule scales stably to a billion-scale pretraining task (GPT-3 XL 1.3B) which is six orders of magnitude larger than its meta-training distribution. Furthermore, it shows strong performance across diverse out-of-distribution tasks and is compatible with modern optimization harness that includes orthogonalization, distinct update rules for input-output and hidden weights, and decoupled weight decay. In all, this work paves the way for practically applicable learnable optimization algorithms, unlocking exploration of richer meta-training and data curation recipes to further improve performance.
</details>

---


### [A Graph Meta-Network for Learning on Kolmogorov-Arnold Networks](https://arxiv.org/abs/2602.16316)
**Authors:** Bar-Shalom, Guy and Tavory, Ami and Evron, Itay and Bechler-Speicher, Maya and Guy, Ido and Maron, Haggai  
**Date:** 2026-02-18 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*International Conference on Learning Representations* · 2026 · [arXiv:2602.16316](https://arxiv.org/abs/2602.16316)

<details>
<summary>Abstract</summary>

> Weight-space models learn directly from the parameters of neural networks, enabling tasks such as predicting their accuracy on new datasets. Naive methods -- like applying MLPs to flattened parameters -- perform poorly, making the design of better weight-space architectures a central challenge. While prior work leveraged permutation symmetries in standard networks to guide such designs, no analogous analysis or tailored architecture yet exists for Kolmogorov-Arnold Networks (KANs). In this work, we show that KANs share the same permutation symmetries as MLPs, and propose the KAN-graph, a graph representation of their computation. Building on this, we develop WS-KAN, the first weight-space architecture that learns on KANs, which naturally accounts for their symmetry. We analyze WS-KAN's expressive power, showing it can replicate an input KAN's forward pass - a standard approach for assessing expressiveness in weight-space architectures. We construct a comprehensive ``zoo'' of trained KANs spanning diverse tasks, which we use as benchmarks to empirically evaluate WS-KAN. Across all tasks, WS-KAN consistently outperforms structure-agnostic baselines, often by a substantial margin. Our code is available at https://github.com/BarSGuy/KAN-Graph-Metanetwork.
</details>

---


### [POP: Prior-Fitted First-Order Optimization Policies](https://arxiv.org/abs/2602.15473)
**Authors:** Kobiolka, Jan and Frey, Christian and Shala, Gresa and Kadra, Arlind and Bedalli, Erind and Grabocka, Josif  
**Date:** 2026-02-17 · **Topics:** General-Purpose Learned Optimizers  
*arXiv.org* · 2026 · [arXiv:2602.15473](https://arxiv.org/abs/2602.15473)

<details>
<summary>Abstract</summary>

> Gradient-based optimizers are highly sensitive to design choices in their adaptive learning rate mechanisms. To address this limitation, we introduce POP, a meta-learned Reinforcement Learning (RL) policy that predicts adaptive learning rates for gradient descent, conditioned on the contextual information provided in the optimization trajectory. Our method introduces a novel RL reward formulation, a new function-scaling strategy for in-distribution generalization, and a novel prior that is used to sample millions of synthetic optimization problems. We evaluate POP on an established benchmark including 43 optimization functions of various complexity, where it significantly outperforms gradient-based methods. Our evaluation demonstrates strong generalization capabilities without task-specific tuning.
</details>

---


### [On the Expressive Power of Permutation-Equivariant Weight-Space Networks](https://arxiv.org/abs/2602.01083)
**Authors:** Dayan, Adir and Eitan, Yam and Maron, Haggai  
**Date:** 2026-02-01 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2026 · [arXiv:2602.01083](https://arxiv.org/abs/2602.01083)

<details>
<summary>Abstract</summary>

> Weight-space learning studies neural architectures that operate directly on the parameters of other neural networks. Motivated by the growing availability of pretrained models, recent work has demonstrated the effectiveness of weight-space networks across a wide range of tasks. SOTA weight-space networks rely on permutation-equivariant designs to improve generalization. However, this may negatively affect expressive power, warranting theoretical investigation. Importantly, unlike other structured domains, weight-space learning targets maps operating on both weight and function spaces, making expressivity analysis particularly subtle. While a few prior works provide partial expressivity results, a comprehensive characterization is still missing. In this work, we address this gap by developing a systematic theory for expressivity of weight-space networks. We first prove that all prominent permutation-equivariant networks are equivalent in expressive power. We then establish universality in both weight- and function-space settings under mild, natural assumptions on the input weights, and characterize the edge-case regimes where universality no longer holds. Guided by our theoretical results, we show that slight modifications to existing weight-space models yield a 34% improvement over prior SOTA, demonstrating the practical relevance of our framework.
</details>

---


### [Ensuring Semantics in Weights of Implicit Neural Representations through the Implicit Function Theorem](https://arxiv.org/abs/2601.23181)
**Authors:** Qiu, Tianming and Sonis, Christos and Shen, Hao  
**Date:** 2026-01-30 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2026 · [arXiv:2601.23181](https://arxiv.org/abs/2601.23181)

<details>
<summary>Abstract</summary>

> Weight Space Learning (WSL), which frames neural network weights as a data modality, is an emerging field with potential for tasks like meta-learning or transfer learning. Particularly, Implicit Neural Representations (INRs) provide a convenient testbed, where each set of weights determines the corresponding individual data sample as a mapping from coordinates to contextual values. So far, a precise theoretical explanation for the mechanism of encoding semantics of data into network weights is still missing. In this work, we deploy the Implicit Function Theorem (IFT) to establish a rigorous mapping between the data space and its latent weight representation space. We analyze a framework that maps instance-specific embeddings to INR weights via a shared hypernetwork, achieving performance competitive with existing baselines on downstream classification tasks across 2D and 3D datasets. These findings offer a theoretical lens for future investigations into network weights.
</details>

---


### [DeepWeightFlow: Re-Basined Flow Matching for Generating Neural Network Weights](https://arxiv.org/abs/2601.05052)
**Authors:** Gupta, Saumya and Biggs, Scott and Laber, Moritz and Shafi, Zohair and Walters, Robin and Paul, Ayan  
**Date:** 2026-01-08 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*The Fourteenth International Conference on Learning Representations (ICLR 2026): https://openreview.net/forum?id=fOwsr1VTi8* · 2026 · [arXiv:2601.05052](https://arxiv.org/abs/2601.05052)

<details>
<summary>Abstract</summary>

> Building efficient and effective generative models for neural network weights has been a research focus of significant interest that faces challenges posed by the high-dimensional weight spaces of modern neural networks and their symmetries. Several prior generative models are limited to generating partial neural network weights, particularly for larger models, such as ResNet and ViT. Those that do generate complete weights struggle with generation speed or require finetuning of the generated models. In this work, we present DeepWeightFlow, a Flow Matching model that operates directly in weight space to generate diverse and high-accuracy neural network weights for a variety of architectures, neural network sizes, and data modalities. The neural networks generated by DeepWeightFlow do not require fine-tuning to perform well and can scale to large networks. We apply Git Re-Basin and TransFusion for neural network canonicalization in the context of generative weight models to account for the impact of neural network permutation symmetries and to improve generation efficiency for larger model sizes. The generated networks excel at transfer learning, and ensembles of hundreds of neural networks can be generated in minutes, far exceeding the efficiency of diffusion-based methods. DeepWeightFlow models pave the way for more efficient and scalable generation of diverse sets of neural networks.
</details>

---


## 2025

### [Metanetworks as Regulatory Operators: Learning to Edit for Requirement Compliance](https://arxiv.org/abs/2512.15469)
**Authors:** Kalogeropoulos, Ioannis and Bouritsas, Giorgos and Panagakis, Yannis  
**Date:** 2025-12-17 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2025 · [arXiv:2512.15469](https://arxiv.org/abs/2512.15469)

<details>
<summary>Abstract</summary>

> As machine learning models are increasingly deployed in high-stakes settings, e.g. as decision support systems in various societal sectors or in critical infrastructure, designers and auditors are facing the need to ensure that models satisfy a wider variety of requirements (e.g. compliance with regulations, fairness, computational constraints) beyond performance. Although most of them are the subject of ongoing studies, typical approaches face critical challenges: post-processing methods tend to compromise performance, which is often counteracted by fine-tuning or, worse, training from scratch, an often time-consuming or even unavailable strategy. This raises the following question: "Can we efficiently edit models to satisfy requirements, without sacrificing their utility?" In this work, we approach this with a unifying framework, in a data-driven manner, i.e. we learn to edit neural networks (NNs), where the editor is an NN itself - a graph metanetwork - and editing amounts to a single inference step. In particular, the metanetwork is trained on NN populations to minimise an objective consisting of two terms: the requirement to be enforced and the preservation of the NN's utility. We experiment with diverse tasks (the data minimisation principle, bias mitigation and weight pruning) improving the trade-offs between performance, requirement satisfaction and time efficiency compared to popular post-processing or re-training alternatives.
</details>

---


### [Learning to Evolve for Optimization via Stability-Inducing Neural Unrolling](https://arxiv.org/abs/2512.11453)
**Authors:** Gao, Jiaxin and Liu, Yaohua and Cheng, Ran and Tan, Kay Chen  
**Date:** 2025-12-12 · **Topics:** Learned Optimizers in Specific Domains  
*arXiv.org* · 2025 · [arXiv:2512.11453](https://arxiv.org/abs/2512.11453)

<details>
<summary>Abstract</summary>

> Evolutionary algorithms serve as a powerful paradigm for tackling optimization challenges, yet their reliance on manually engineered heuristics inherently limits their adaptability across diverse landscapes. However, the transition from the hand-crafted heuristics to data-driven algorithms faces a fundamental dilemma: achieving neural \emphplasticity without sacrificing algorithmic stability. Although learned optimizers offer high adaptivity, their unconstrained update rules often result in unstable dynamics and brittle generalization on unseen landscapes. To address this challenge, this paper proposes Learning to Evolve (L2E), a bilevel meta-optimization framework that learns evolutionary search via stability-inducing neural unrolling. First, L2E reformulates population evolution as an unrolled fixed-point iteration via a structured neural operator. In this design, the inner loop imposes a stability-biased update structure, while the outer loop meta-trains the operator to produce effective search trajectories across tasks. Second, to balance global exploration with local refinement, a gradient-derived composite solver adaptively fuses learned evolutionary proposals with proxy numerical guidance in a differentiable manner. Extensive experiments on synthetic benchmarks and real-world control tasks demonstrate that L2E achieves substantial optimization performance, scales to high-dimensional problems, and exhibits robust zero-shot transfer across diverse test distributions.
</details>

---


### [Weight Space Representation Learning via Neural Field Adaptation](https://arxiv.org/abs/2512.01759)
**Authors:** Yang, Zhuoqian and Salzmann, Mathieu and Süsstrunk, Sabine  
**Date:** 2025-12-01 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*CVPR 2026* · 2025 · [arXiv:2512.01759](https://arxiv.org/abs/2512.01759)

<details>
<summary>Abstract</summary>

> We investigate the potential of weights to serve as effective representations, focusing on neural fields. Our key insight is that constraining the optimization space through a pre-trained base model and low-rank adaptation (LoRA) can induce structure in weight space. Across reconstruction, generation, and analysis tasks on 2D and 3D data, we find that multiplicative LoRA weights achieve high representation quality while exhibiting distinctiveness and semantic structure. When used with latent diffusion models, multiplicative LoRA weights enable higher-quality generation than existing weight-space methods.
</details>

---


### [Symmetry-Aware Graph Metanetwork Autoencoders: Model Merging through Parameter Canonicalization](https://arxiv.org/abs/2511.12601)
**Authors:** Boufalis, Odysseas and Carrasco-Pollo, Jorge and Rosenthal, Joshua and Terres-Caballero, Eduardo and García-Castellanos, Alejandro  
**Date:** 2025-11-16 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2025 · [arXiv:2511.12601](https://arxiv.org/abs/2511.12601)

<details>
<summary>Abstract</summary>

> Neural network parameterizations exhibit inherent symmetries that yield multiple equivalent minima within the loss landscape. Scale Graph Metanetworks (ScaleGMNs) explicitly leverage these symmetries by proposing an architecture equivariant to both permutation and parameter scaling transformations. Previous work by Ainsworth et al. (2023) addressed permutation symmetries through a computationally intensive combinatorial assignment problem, demonstrating that leveraging permutation symmetries alone can map networks into a shared loss basin. In this work, we extend their approach by also incorporating scaling symmetries, presenting an autoencoder framework utilizing ScaleGMNs as invariant encoders. Experimental results demonstrate that our method aligns Implicit Neural Representations (INRs) and Convolutional Neural Networks (CNNs) under both permutation and scaling symmetries without explicitly solving the assignment problem. This approach ensures that similar networks naturally converge within the same basin, facilitating model merging, i.e., smooth linear interpolation while avoiding regions of high loss. The code is publicly available on our GitHub repository.
</details>

---


### [Enhancing Fractional Gradient Descent with Learned Optimizers](https://arxiv.org/abs/2510.18783)
**Authors:** Sobotka, Jan and Šimánek, Petr and Kordík, Pavel  
**Date:** 2025-10-21 · **Topics:** General-Purpose Learned Optimizers  
*arXiv.org* · 2025 · [arXiv:2510.18783](https://arxiv.org/abs/2510.18783)

<details>
<summary>Abstract</summary>

> Fractional Gradient Descent (FGD) offers a novel and promising way to accelerate optimization by incorporating fractional calculus into machine learning. Although FGD has shown encouraging initial results across various optimization tasks, it faces significant challenges with convergence behavior and hyperparameter selection. Moreover, the impact of its hyperparameters is not fully understood, and scheduling them is particularly difficult in non-convex settings such as neural network training. To address these issues, we propose a novel approach called Learning to Optimize Caputo Fractional Gradient Descent (L2O-CFGD), which meta-learns how to dynamically tune the hyperparameters of Caputo FGD (CFGD). Our method's meta-learned schedule outperforms CFGD with static hyperparameters found through an extensive search and, in some tasks, achieves performance comparable to a fully black-box meta-learned optimizer. L2O-CFGD can thus serve as a powerful tool for researchers to identify high-performing hyperparameters and gain insights on how to leverage the history-dependence of the fractional differential in optimization.
</details>

---


### [Learning Regularizers: Learning Optimizers that can Regularize](https://arxiv.org/abs/2510.08968)
**Authors:** Sahoo, Suraj Kumar and Krishnan, Narayanan C  
**Date:** 2025-10-10 · **Topics:** General-Purpose Learned Optimizers  
*arXiv.org* · 2025 · [arXiv:2510.08968](https://arxiv.org/abs/2510.08968)

<details>
<summary>Abstract</summary>

> Learned Optimizers (LOs), a type of Meta-learning, have gained traction due to their ability to be parameterized and trained for efficient optimization. Traditional gradient-based methods incorporate explicit regularization techniques such as Sharpness-Aware Minimization (SAM), Gradient-norm Aware Minimization (GAM), and Gap-guided Sharpness-Aware Minimization (GSAM) to enhance generalization and convergence. In this work, we explore a fundamental question: \textbfCan regularizers be learned? We empirically demonstrate that LOs can be trained to learn and internalize the effects of traditional regularization techniques without explicitly applying them to the objective function. We validate this through extensive experiments on standard benchmarks (including MNIST, FMNIST, CIFAR and Neural Networks such as MLP, MLP-Relu and CNN), comparing LOs trained with and without access to explicit regularizers. Regularized LOs consistently outperform their unregularized counterparts in terms of test accuracy and generalization. Furthermore, we show that LOs retain and transfer these regularization effects to new optimization tasks by inherently seeking minima similar to those targeted by these regularizers. Our results suggest that LOs can inherently learn regularization properties, \textitchallenging the conventional necessity of explicit optimizee loss regularization.
</details>

---


### [Symmetry-Aware Fully-Amortized Optimization with Scale Equivariant Graph Metanetworks](https://arxiv.org/abs/2510.08300) — 🔗 *LO-linked*
**Authors:** Kuipers, Bart and Byrman, Freek and Uyterlinde, Daniel and García-Castellanos, Alejandro  
**Date:** 2025-10-09 · **Topics:** Weight-Space Learning & Graph Metanetworks, General-Purpose Learned Optimizers  
*arXiv.org* · 2025 · [arXiv:2510.08300](https://arxiv.org/abs/2510.08300)

<details>
<summary>Abstract</summary>

> Amortized optimization accelerates the solution of related optimization problems by learning mappings that exploit shared structure across problem instances. We explore the use of Scale Equivariant Graph Metanetworks (ScaleGMNs) for this purpose. By operating directly in weight space, ScaleGMNs enable single-shot fine-tuning of existing models, reducing the need for iterative optimization. We demonstrate the effectiveness of this approach empirically and provide a theoretical result: the gauge freedom induced by scaling symmetries is strictly smaller in convolutional neural networks than in multi-layer perceptrons. This insight helps explain the performance differences observed between architectures in both our work and that of Kalogeropoulos et al. (2024). Overall, our findings underscore the potential of symmetry-aware metanetworks as a powerful approach for efficient and generalizable neural network optimization. Open-source code: https://github.com/daniuyter/scalegmn_amortization
</details>

---


### [Learning Model Representations Using Publicly Available Model Hubs](https://arxiv.org/abs/2510.02096)
**Authors:** Falk, Damian and Schürholt, Konstantin and Tzevelekakis, Konstantinos and Meynent, Léo and Borth, Damian  
**Date:** 2025-10-02 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2025 · [arXiv:2510.02096](https://arxiv.org/abs/2510.02096)

<details>
<summary>Abstract</summary>

> The weights of neural networks have emerged as a novel data modality, giving rise to the field of weight space learning. A central challenge in this area is that learning meaningful representations of weights typically requires large, carefully constructed collections of trained models, typically referred to as model zoos. These model zoos are often trained ad-hoc, requiring large computational resources, constraining the learned weight space representations in scale and flexibility. In this work, we drop this requirement by training a weight space learning backbone on arbitrary models downloaded from large, unstructured model repositories such as Hugging Face. Unlike curated model zoos, these repositories contain highly heterogeneous models: they vary in architecture and dataset, and are largely undocumented. To address the methodological challenges posed by such heterogeneity, we propose a new weight space backbone designed to handle unstructured model populations. We demonstrate that weight space representations trained on models from Hugging Face achieve strong performance, often outperforming backbones trained on laboratory-generated model zoos. Finally, we show that the diversity of the model weights in our training set allows our weight space model to generalize to unseen data modalities. By demonstrating that high-quality weight space representations can be learned in the wild, we show that curated model zoos are not indispensable, thereby overcoming a strong limitation currently faced by the weight space learning community.
</details>

---


### [LeOp-GS: Learned Optimizer With Dynamic Gradient Update for Sparse-View 3DGS](https://doi.org/10.1109/tvcg.2025.3616156)
**Authors:** Lei, Xinyu and Wang, Xuan and Liu, Longjun and Li, Haoteng and Zhang, Haonan  
**Date:** 2025-10-02 · **Topics:** Learned Optimizers in Specific Domains  
*IEEE Transactions on Visualization and Computer Graphics* · 2025

<details>
<summary>Abstract</summary>

> 3D Gaussian Splatting (3DGS) achieves remarkable speed and performance in novel view synthesis but suffers from overfitting and degraded reconstruction when handling sparse-view inputs. This paper innovatively addresses this challenge from a learning-to-optimize perspective by leveraging a learned optimizer (i.e., a multi-layer perceptron, MLP) to update the relevant parameters of 3DGS during the optimization process. Evidently, using a single MLP to handle all optimization variables, whose numbers may even vary during the optimization process, is impossible. Therefore, we present a point-wise position-aware optimizer that updates the parameters for each 3DGS point individually. Specifically, it takes the point coordinates and corresponding parameter values as input to predict the updates, thereby allowing efficient and adaptive optimization. In the case of sparse view modeling, the learned optimizer imposes position-aware constraints on the parameter updates during optimization. This effectively encourages the relevant parameters to converge stably to better solutions. To update the optimizer's parameters, we propose a dynamic gradient update strategy based on spatial perturbation and weighted fusion, enabling the optimizer to capture broader contextual information. Experiments demonstrate that our method effectively addresses the problem of modeling 3DGS from sparse training views, achieving state-of-the-art results across multiple datasets.
</details>

---


### [Text2Weight: Bridging Natural Language and Neural Network Weight Spaces](https://arxiv.org/abs/2508.13633)
**Authors:** Tian, Bowen and Chen, Wenshuo and Li, Zexi and Lai, Songning and Wu, Jiemin and Yue, Yutao  
**Date:** 2025-08-19 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*ACM International Conference on Multimedia (ACM MM)* · 2025 · [arXiv:2508.13633](https://arxiv.org/abs/2508.13633)

<details>
<summary>Abstract</summary>

> How far are we really from automatically generating neural networks? While neural network weight generation shows promise, current approaches struggle with generalization to unseen tasks and practical application exploration. To address this, we propose T2W, a diffusion transformer framework that generates task-specific weights conditioned on natural language descriptions. T2W hierarchically processes network parameters into uniform blocks, integrates text embeddings from CLIP via a prior attention mechanism, and employs adversarial training with weight-space augmentation to enhance generalization. Experiments on Cifar100, Caltech256, and TinyImageNet demonstrate T2W's ability to produce high-quality weights for unseen tasks, outperforming optimization-based initialization and enabling novel applications such as weight enhancement and text-guided model fusion. Our work bridges textual semantics with weight-space dynamics, supported by an open-source dataset of text-weight pairs, advancing the practicality of generative models in neural network parameter synthesis. Our code is available on Github.
</details>

---


### [L-SR1: Learned Symmetric-Rank-One Preconditioning](https://arxiv.org/abs/2508.12270)
**Authors:** Lifshitz, Gal and Zuler, Shahar and Fouks, Ori and Raviv, Dan  
**Date:** 2025-08-17 · **Topics:** General-Purpose Learned Optimizers  
*arXiv.org* · 2025 · [arXiv:2508.12270](https://arxiv.org/abs/2508.12270)

<details>
<summary>Abstract</summary>

> End-to-end deep learning has achieved impressive results but often relies on large labeled datasets, exhibits limited generalization to unseen scenarios, and incurs substantial computational cost. Classical optimization methods, in contrast, are more data-efficient and lightweight but frequently suffer from slow convergence. Learned optimizers aim to bridge this gap, yet existing approaches have focused primarily on first-order methods, while learned second-order optimization has received much less attention. We introduce L-SR1, a learned second-order optimizer inspired by the classical Symmetric Rank-One (SR1) method. At its core, L-SR1 employs a Projection-Guided Secant Mechanism (PGSM) that generates positive semi-definite preconditioners and biases meta-training toward the quasi-Newton secant relation. Through controlled analytic benchmarks, we study stability, generalization across problem dimensions, and search direction quality, and further evaluate L-SR1 on Monocular Human Mesh Recovery (HMR), where it outperforms both classical and learned optimization-based baselines. With a compact model and no reliance on task-specific fine-tuning or annotated data, L-SR1 demonstrates strong generalization and can be integrated into a broad range of iterative optimization problems to accelerate convergence and reduce the required number of iterations.
</details>

---


### [Flows and Diffusions on the Neural Manifold](https://arxiv.org/abs/2507.10623)
**Authors:** Saragih, Daniel and Cao, Deyu and Balaji, Tejas  
**Date:** 2025-07-14 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2025 · [arXiv:2507.10623](https://arxiv.org/abs/2507.10623)

<details>
<summary>Abstract</summary>

> Diffusion and flow-based generative models have achieved remarkable success in domains such as image synthesis, video generation, and natural language modeling. In this work, we extend these advances to weight space learning by leveraging recent techniques to incorporate structural priors derived from optimization dynamics. Central to our approach is modeling the trajectory induced by gradient descent as a trajectory inference problem. We unify several trajectory inference techniques towards matching a gradient flow, providing a theoretical framework for treating optimization paths as inductive bias. We further explore architectural and algorithmic choices, including reward fine-tuning by adjoint matching, the use of autoencoders for latent weight representation, conditioning on task-specific context data, and adopting informative source distributions such as Kaiming uniform. Experiments demonstrate that our method matches or surpasses baselines in generating in-distribution weights, improves initialization for downstream training, and supports fine-tuning to enhance performance. Finally, we illustrate a practical application in safety-critical systems: detecting harmful covariate shifts, where our method outperforms the closest comparable baseline.
</details>

---


### [GradMetaNet: An Equivariant Architecture for Learning on Gradients](https://arxiv.org/abs/2507.01649) — 🔗 *LO-linked*
**Authors:** Gelberg, Yoav and Eitan, Yam and Navon, Aviv and Shamsian, Aviv and Putterman, Theo and Bronstein, Michael and Maron, Haggai  
**Date:** 2025-07-02 · **Topics:** Weight-Space Learning & Graph Metanetworks, General-Purpose Learned Optimizers  
*neural information processing systems* · 2025 · [arXiv:2507.01649](https://arxiv.org/abs/2507.01649)

<details>
<summary>Abstract</summary>

> Gradients of neural networks encode valuable information for optimization, editing, and analysis of models. Therefore, practitioners often treat gradients as inputs to task-specific algorithms, e.g. for pruning or optimization. Recent works explore learning algorithms that operate directly on gradients but use architectures that are not specifically designed for gradient processing, limiting their applicability. In this paper, we present a principled approach for designing architectures that process gradients. Our approach is guided by three principles: (1) equivariant design that preserves neuron permutation symmetries, (2) processing sets of gradients across multiple data points to capture curvature information, and (3) efficient gradient representation through rank-1 decomposition. Based on these principles, we introduce GradMetaNet, a novel architecture for learning on gradients, constructed from simple equivariant blocks. We prove universality results for GradMetaNet, and show that previous approaches cannot approximate natural gradient-based functions that GradMetaNet can. We then demonstrate GradMetaNet's effectiveness on a diverse set of gradient-based tasks on MLPs and transformers, such as learned optimization, INR editing, and estimating loss landscape curvature.
</details>

---


### [Symmetry in Neural Network Parameter Spaces](https://arxiv.org/abs/2506.13018)
**Authors:** Zhao, Bo and Walters, Robin and Yu, Rose  
**Date:** 2025-06-16 · **Topics:** Surveys, Tutorials & Benchmarks, Weight-Space Learning & Graph Metanetworks  
*Transactions on machine learning research* · 2025 · [arXiv:2506.13018](https://arxiv.org/abs/2506.13018)

<details>
<summary>Abstract</summary>

> Modern deep learning models are highly overparameterized, resulting in large sets of parameter configurations that yield the same outputs. A significant portion of this redundancy is explained by symmetries in the parameter space--transformations that leave the network function unchanged. These symmetries shape the loss landscape and constrain learning dynamics, offering a new lens for understanding optimization, generalization, and model complexity that complements existing theory of deep learning. This survey provides an overview of parameter space symmetry. We summarize existing literature, uncover connections between symmetry and learning theory, and identify gaps and opportunities in this emerging field.
</details>

---


### [PyLO: Towards Accessible Learned Optimizers in PyTorch](https://www.semanticscholar.org/paper/9e537b053ee3b3b8fa3ada451944ea611c347efe)
**Authors:** Janson, Paul and Therien, Benjamin and Anthony, Quentin and Huang, Xiaolong and Moudgil, Abhinav and Belilovsky, Eugene  
**Date:** 2025-06-12 · **Topics:** General-Purpose Learned Optimizers  
*arXiv.org* · 2025 · [arXiv:2506.10315](https://arxiv.org/abs/2506.10315)

<details>
<summary>Abstract</summary>

> Learned optimizers have been an active research topic over the past decade, with increasing progress toward practical, general-purpose optimizers that can serve as drop-in replacements for widely used methods like Adam. However, recent advances -- such as VeLO, which was meta-trained for 4000 TPU-months -- remain largely inaccessible to the broader community, in part due to their reliance on JAX and the absence of user-friendly packages for applying the optimizers after meta-training. To address this gap, we introduce PyLO, a PyTorch-based library that brings learned optimizers to the broader machine learning community through familiar, widely adopted workflows. Unlike prior work focused on synthetic or convex tasks, our emphasis is on applying learned optimization to real-world large-scale pre-training tasks. Our release includes a CUDA-accelerated version of the small_fc_lopt learned optimizer architecture from (Metz et al., 2022a), delivering substantial speedups -- from 39.36 to 205.59 samples/sec throughput for training ViT B/16 with batch size 32. PyLO also allows us to easily combine learned optimizers with existing optimization tools such as learning rate schedules and weight decay. When doing so, we find that learned optimizers can substantially benefit. Our code is available at https://github.com/Belilovsky-Lab/pylo
</details>

---


### [Generative Modeling of Weights: Generalization or Memorization?](https://arxiv.org/abs/2506.07998)
**Authors:** Zeng, Boya and Yin, Yida and Xu, Zhiqiu and Liu, Zhuang  
**Date:** 2025-06-09 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2025 · [arXiv:2506.07998](https://arxiv.org/abs/2506.07998)

<details>
<summary>Abstract</summary>

> Generative models have recently been explored for synthesizing neural network weights. These approaches take neural network checkpoints as training data and aim to generate high-performing weights during inference. In this work, we examine four representative, well-known methods on their ability to generate novel model weights, i.e., weights that are different from the checkpoints seen during training. Contrary to claims in prior work, we find that these methods synthesize weights largely by memorization: they produce either replicas, or, at best, simple interpolations of the training checkpoints. Moreover, they fail to outperform simple baselines, such as adding noise to the weights or taking a simple weight ensemble, in obtaining different and simultaneously high-performing models. Our further analysis suggests that this memorization might result from limited data, overparameterized models, and the underuse of structural priors specific to weight data. These findings highlight the need for more careful design and rigorous evaluation of generative models when applied to new domains. Our code is available at https://github.com/boyazeng/weight_memorization.
</details>

---


### [Gradient Flow Matching for Learning Update Dynamics in Neural Network Training](https://arxiv.org/abs/2505.20221)
**Authors:** Shou, Xiao and Ding, Yanna and Gao, Jianxi  
**Date:** 2025-05-26 · **Topics:** General-Purpose Learned Optimizers  
*arXiv.org* · 2025 · [arXiv:2505.20221](https://arxiv.org/abs/2505.20221)

<details>
<summary>Abstract</summary>

> Training deep neural networks remains computationally intensive due to the itera2 tive nature of gradient-based optimization. We propose Gradient Flow Matching (GFM), a continuous-time modeling framework that treats neural network training as a dynamical system governed by learned optimizer-aware vector fields. By leveraging conditional flow matching, GFM captures the underlying update rules of optimizers such as SGD, Adam, and RMSprop, enabling smooth extrapolation of weight trajectories toward convergence. Unlike black-box sequence models, GFM incorporates structural knowledge of gradient-based updates into the learning objective, facilitating accurate forecasting of final weights from partial training sequences. Empirically, GFM achieves forecasting accuracy that is competitive with Transformer-based models and significantly outperforms LSTM and other classical baselines. Furthermore, GFM generalizes across neural architectures and initializations, providing a unified framework for studying optimization dynamics and accelerating convergence prediction.
</details>

---


### [Meta Pruning via Graph Metanetworks : A Universal Meta Learning Framework for Network Pruning](https://arxiv.org/abs/2506.12041)
**Authors:** Liu, Yewei and Wang, Xiyuan and Zhang, Muhan  
**Date:** 2025-05-24 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2025 · [arXiv:2506.12041](https://arxiv.org/abs/2506.12041)

<details>
<summary>Abstract</summary>

> We propose an entirely new meta-learning framework for network pruning. It is a general framework that can be theoretically applied to almost all types of networks with all kinds of pruning and has great generality and transferability. Experiments have shown that it can achieve outstanding results on many popular and representative pruning tasks (including both CNNs and Transformers). Unlike all prior works that either rely on fixed, hand-crafted criteria to prune in a coarse manner, or employ learning to prune ways that require special training during each pruning and lack generality. Our framework can learn complex pruning rules automatically via a neural network (metanetwork) and has great generality that can prune without any special training. More specifically, we introduce the newly developed idea of metanetwork from meta-learning into pruning. A metanetwork is a network that takes another network as input and produces a modified network as output. In this paper, we first establish a bijective mapping between neural networks and graphs, and then employ a graph neural network as our metanetwork. We train a metanetwork that learns the pruning strategy automatically and can transform a network that is hard to prune into another network that is much easier to prune. Once the metanetwork is trained, our pruning needs nothing more than a feedforward through the metanetwork and some standard finetuning to prune at state-of-the-art. Our code is available at https://github.com/Yewei-Liu/MetaPruning
</details>

---


### [Generative Adaptation of Dynamics to Environmental Shifts via Weight-space Diffusion](https://arxiv.org/abs/2505.13919)
**Authors:** Li, Ruikun and Wang, Huandong and Ding, Jingtao and Yuan, Yuan and Liao, Qingmin and Li, Yong  
**Date:** 2025-05-20 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2025 · [arXiv:2505.13919](https://arxiv.org/abs/2505.13919)

<details>
<summary>Abstract</summary>

> Data-driven dynamics prediction often fails under environmental shifts, while traditional fine-tuning remains computationally prohibitive for hardware-constrained or data-scarce applications. We propose DynaDiff, a generative meta-learning framework that transitions the paradigm from gradient-based tuning or modulation to direct weight-space generation. Specifically, we first abstract expert weights as novel weight graphs, utilizing multi-head attention to explicitly capture topological coupling within weights. Subsequently, we design a functional loss to ensure that the generated models achieve consistency with expert models in physical behavior. Finally, we develop a dynamics-informed prompter that extracts cross-domain physical and spectral features from observation sequences to condition the diffusion model. Experiments demonstrate that DynaDiff boosts average prediction accuracy by 10.78% over competitive baselines. Furthermore, by pre-constructing a model zoo of expert predictors, we amortize the fine-tuning overhead into a one-time offline cost, significantly boosting deployment efficiency in new environments.
</details>

---


### [A Model Zoo on Phase Transitions in Neural Networks](https://arxiv.org/abs/2504.18072)
**Authors:** Schürholt, Konstantin and Meynent, Léo and Zhou, Yefan and Lu, Haiquan and Yang, Yaoqing and Borth, Damian  
**Date:** 2025-04-25 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2025 · [arXiv:2504.18072](https://arxiv.org/abs/2504.18072)

<details>
<summary>Abstract</summary>

> Using the weights of trained Neural Network (NN) models as data modality has recently gained traction as a research field - dubbed Weight Space Learning (WSL). Multiple recent works propose WSL methods to analyze models, evaluate methods, or synthesize weights. Weight space learning methods require populations of trained models as datasets for development and evaluation. However, existing collections of models - called `model zoos' - are unstructured or follow a rudimentary definition of diversity. In parallel, work rooted in statistical physics has identified phases and phase transitions in NN models. Models are homogeneous within the same phase but qualitatively differ from one phase to another. We combine the idea of `model zoos' with phase information to create a controlled notion of diversity in populations. We introduce 12 large-scale zoos that systematically cover known phases and vary over model architecture, size, and datasets. These datasets cover different modalities, such as computer vision, natural language processing, and scientific ML. For every model, we compute loss landscape metrics and validate full coverage of the phases. With this dataset, we provide the community with a resource with a wide range of potential applications for WSL and beyond. Evidence suggests the loss landscape phase plays a role in applications such as model training, analysis, or sparsification. We demonstrate this in an exploratory study of the downstream methods like transfer learning or model weights averaging.
</details>

---


### [Improving Learning to Optimize Using Parameter Symmetries](https://arxiv.org/abs/2504.15399) — 🔗 *LO-linked*
**Authors:** Zamir, Guy and Dokania, Aryan and Zhao, Bo and Yu, Rose  
**Date:** 2025-04-21 · **Topics:** General-Purpose Learned Optimizers, Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2025 · [arXiv:2504.15399](https://arxiv.org/abs/2504.15399)

<details>
<summary>Abstract</summary>

> We analyze a learning-to-optimize (L2O) algorithm that exploits parameter space symmetry to enhance optimization efficiency. Prior work has shown that jointly learning symmetry transformations and local updates improves meta-optimizer performance. Supporting this, our theoretical analysis demonstrates that even without identifying the optimal group element, the method locally resembles Newton's method. We further provide an example where the algorithm provably learns the correct symmetry transformation during training. To empirically evaluate L2O with teleportation, we introduce a benchmark, analyze its success and failure cases, and show that enhancements like momentum further improve performance. Our results highlight the potential of leveraging neural network parameter space symmetry to advance meta-optimization.
</details>

---


### [The Impact of Model Zoo Size and Composition on Weight Space Learning](https://arxiv.org/abs/2504.10141)
**Authors:** Falk, Damian and Schürholt, Konstantin and Borth, Damian  
**Date:** 2025-04-14 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2025 · [arXiv:2504.10141](https://arxiv.org/abs/2504.10141)

<details>
<summary>Abstract</summary>

> Re-using trained neural network models is a common strategy to reduce training cost and transfer knowledge. Weight space learning - using the weights of trained models as data modality - is a promising new field to re-use populations of pre-trained models for future tasks. Approaches in this field have demonstrated high performance both on model analysis and weight generation tasks. However, until now their learning setup requires homogeneous model zoos where all models share the same exact architecture, limiting their capability to generalize beyond the population of models they saw during training. In this work, we remove this constraint and propose a modification to a common weight space learning method to accommodate training on heterogeneous populations of models. We further investigate the resulting impact of model diversity on generating unseen neural network model weights for zero-shot knowledge transfer. Our extensive experimental evaluation shows that including models with varying underlying image datasets has a high impact on performance and generalization, for both in- and out-of-distribution settings. Code is available on github.com/HSG-AIML/MultiZoo-SANE.
</details>

---


### [A Model Zoo of Vision Transformers](https://arxiv.org/abs/2504.10231)
**Authors:** Falk, Damian and Meynent, Léo and Pfammatter, Florence and Schürholt, Konstantin and Borth, Damian  
**Date:** 2025-04-14 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2025 · [arXiv:2504.10231](https://arxiv.org/abs/2504.10231)

<details>
<summary>Abstract</summary>

> The availability of large, structured populations of neural networks - called 'model zoos' - has led to the development of a multitude of downstream tasks ranging from model analysis, to representation learning on model weights or generative modeling of neural network parameters. However, existing model zoos are limited in size and architecture and neglect the transformer, which is among the currently most successful neural network architectures. We address this gap by introducing the first model zoo of vision transformers (ViT). To better represent recent training approaches, we develop a new blueprint for model zoo generation that encompasses both pre-training and fine-tuning steps, and publish 250 unique models. They are carefully generated with a large span of generating factors, and their diversity is validated using a thorough choice of weight-space and behavioral metrics. To further motivate the utility of our proposed dataset, we suggest multiple possible applications grounded in both extensive exploratory experiments and a number of examples from the existing literature. By extending previous lines of similar work, our model zoo allows researchers to push their model population-based methods from the small model regime to state-of-the-art architectures. We make our model zoo available at github.com/ModelZoos/ViTModelZoo.
</details>

---


### [Geometric Flow Models over Neural Network Weights](https://arxiv.org/abs/2504.03710) — 🔗 *LO-linked*
**Authors:** Erdogan, Ege  
**Date:** 2025-03-27 · **Topics:** Weight-Space Learning & Graph Metanetworks, General-Purpose Learned Optimizers  
*arXiv.org* · 2025 · [arXiv:2504.03710](https://arxiv.org/abs/2504.03710)

<details>
<summary>Abstract</summary>

> Deep generative models such as flow and diffusion models have proven to be effective in modeling high-dimensional and complex data types such as videos or proteins, and this has motivated their use in different data modalities, such as neural network weights. A generative model of neural network weights would be useful for a diverse set of applications, such as Bayesian deep learning, learned optimization, and transfer learning. However, the existing work on weight-space generative models often ignores the symmetries of neural network weights, or only takes into account a subset of them. Modeling those symmetries, such as permutation symmetries between subsequent layers in an MLP, the filters in a convolutional network, or scaling symmetries arising with the use of non-linear activations, holds the potential to make weight-space generative modeling more efficient by effectively reducing the dimensionality of the problem. In this light, we aim to design generative models in weight-space that more comprehensively respect the symmetries of neural network weights. We build on recent work on generative modeling with flow matching, and weight-space graph neural networks to design three different weight-space flows. Each of our flows takes a different approach to modeling the geometry of neural network weights, and thus allows us to explore the design space of weight-space flows in a principled way. Our results confirm that modeling the geometry of neural networks more faithfully leads to more effective flow models that can generalize to different tasks and architectures, and we show that while our flows obtain competitive performance with orders of magnitude fewer parameters than previous work, they can be further improved by scaling them up. We conclude by listing potential directions for future work on weight-space generative models.
</details>

---


### [Shape Generation via Weight Space Learning](https://arxiv.org/abs/2503.21830)
**Authors:** Plattner, Maximilian and Berzins, Arturs and Brandstetter, Johannes  
**Date:** 2025-03-26 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2025 · [arXiv:2503.21830](https://arxiv.org/abs/2503.21830)

<details>
<summary>Abstract</summary>

> Foundation models for 3D shape generation have recently shown a remarkable capacity to encode rich geometric priors across both global and local dimensions. However, leveraging these priors for downstream tasks can be challenging as real-world data are often scarce or noisy, and traditional fine-tuning can lead to catastrophic forgetting. In this work, we treat the weight space of a large 3D shape-generative model as a data modality that can be explored directly. We hypothesize that submanifolds within this high-dimensional weight space can modulate topological properties or fine-grained part features separately, demonstrating early-stage evidence via two experiments. First, we observe a sharp phase transition in global connectivity when interpolating in conditioning space, suggesting that small changes in weight space can drastically alter topology. Second, we show that low-dimensional reparameterizations yield controlled local geometry changes even with very limited data. These results highlight the potential of weight space learning to unlock new approaches for 3D shape generation and specialized fine-tuning.
</details>

---


### [Structure Is Not Enough: Leveraging Behavior for Neural Network Weight Reconstruction](https://arxiv.org/abs/2503.17138)
**Authors:** Meynent, Léo and Melev, Ivan and Schürholt, Konstantin and Kauermann, Göran and Borth, Damian  
**Date:** 2025-03-21 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2025 · [arXiv:2503.17138](https://arxiv.org/abs/2503.17138)

<details>
<summary>Abstract</summary>

> The weights of neural networks (NNs) have recently gained prominence as a new data modality in machine learning, with applications ranging from accuracy and hyperparameter prediction to representation learning or weight generation. One approach to leverage NN weights involves training autoencoders (AEs), using contrastive and reconstruction losses. This allows such models to be applied to a wide variety of downstream tasks, and they demonstrate strong predictive performance and low reconstruction error. However, despite the low reconstruction error, these AEs reconstruct NN models with deteriorated performance compared to the original ones, limiting their usability with regard to model weight generation. In this paper, we identify a limitation of weight-space AEs, specifically highlighting that a structural loss, that uses the Euclidean distance between original and reconstructed weights, fails to capture some features critical for reconstructing high-performing models. We analyze the addition of a behavioral loss for training AEs in weight space, where we compare the output of the reconstructed model with that of the original one, given some common input. We show a strong synergy between structural and behavioral signals, leading to increased performance in all downstream tasks evaluated, in particular NN weights reconstruction and generation.
</details>

---


### [Make Optimization Once and for All with Fine-grained Guidance](https://arxiv.org/abs/2503.11462)
**Authors:** Shi, Mingjia and Lin, Ruihan and Chen, Xuxi and Zhou, Yuhao and Ding, Zezhen and Li, Pingzhi and Wang, Tong and Wang, Kai and Wang, Zhangyang and Zhang, Jiheng and Chen, Tianlong  
**Date:** 2025-03-14 · **Topics:** General-Purpose Learned Optimizers  
*arXiv.org* · 2025 · [arXiv:2503.11462](https://arxiv.org/abs/2503.11462)

<details>
<summary>Abstract</summary>

> Learning to Optimize (L2O) enhances optimization efficiency with integrated neural networks. L2O paradigms achieve great outcomes, e.g., refitting optimizer, generating unseen solutions iteratively or directly. However, conventional L2O methods require intricate design and rely on specific optimization processes, limiting scalability and generalization. Our analyses explore general framework for learning optimization, called Diff-L2O, focusing on augmenting sampled solutions from a wider view rather than local updates in real optimization process only. Meanwhile, we give the related generalization bound, showing that the sample diversity of Diff-L2O brings better performance. This bound can be simply applied to other fields, discussing diversity, mean-variance, and different tasks. Diff-L2O's strong compatibility is empirically verified with only minute-level training, comparing with other hour-levels.
</details>

---


### [We Should Chart an Atlas of All the World's Models](https://arxiv.org/abs/2503.10633)
**Authors:** Horwitz, Eliahu and Kurer, Nitzan and Kahana, Jonathan and Amar, Liel and Hoshen, Yedid  
**Date:** 2025-03-13 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*neural information processing systems* · 2025 · [arXiv:2503.10633](https://arxiv.org/abs/2503.10633)

<details>
<summary>Abstract</summary>

> Public model repositories now contain millions of models, yet most models remain undocumented and effectively lost. In this position paper, we advocate for charting the world's model population in a unified structure we call the Model Atlas: a graph that captures models, their attributes, and the weight transformations that connect them. The Model Atlas enables applications in model forensics, meta-ML research, and model discovery, challenging tasks given today's unstructured model repositories. However, because most models lack documentation, large atlas regions remain uncharted. Addressing this gap motivates new machine learning methods that treat models themselves as data, inferring properties such as functionality, performance, and lineage directly from their weights. We argue that a scalable path forward is to bypass the unique parameter symmetries that plague model weights. Charting all the world's models will require a community effort, and we hope its broad utility will rally researchers toward this goal.
</details>

---


### [On the Internal Representations of Graph Metanetworks](https://arxiv.org/abs/2503.09120)
**Authors:** Yeom, Taesun and Lee, Jaeho  
**Date:** 2025-03-12 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2025 · [arXiv:2503.09120](https://arxiv.org/abs/2503.09120)

<details>
<summary>Abstract</summary>

> Weight space learning is an emerging paradigm in the deep learning community. The primary goal of weight space learning is to extract informative features from a set of parameters using specially designed neural networks, often referred to as \emphmetanetworks. However, it remains unclear how these metanetworks learn solely from parameters. To address this, we take the first step toward understanding \emphrepresentations of metanetworks, specifically graph metanetworks (GMNs), which achieve state-of-the-art results in this field, using centered kernel alignment (CKA). Through various experiments, we reveal that GMNs and general neural networks (\textite.g., multi-layer perceptrons (MLPs) and convolutional neural networks (CNNs)) differ in terms of their representation space.
</details>

---


### [Adversarial Attacks in Weight-Space Classifiers](https://arxiv.org/abs/2502.20314)
**Authors:** Shor, Tamir and Fetaya, Ethan and Baskin, Chaim and Bronstein, Alex  
**Date:** 2025-02-27 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*Transactions on machine learning research* · 2025 · [arXiv:2502.20314](https://arxiv.org/abs/2502.20314)

<details>
<summary>Abstract</summary>

> Implicit Neural Representations (INRs) have been recently garnering increasing interest in various research fields, mainly due to their ability to represent large, complex data in a compact, continuous manner. Past work further showed that numerous popular downstream tasks can be performed directly in the INR parameter-space. Doing so can substantially reduce the computational resources required to process the represented data in their native domain. A major difficulty in using modern machine-learning approaches, is their high susceptibility to adversarial attacks, which have been shown to greatly limit the reliability and applicability of such methods in a wide range of settings. In this work, we perform an in-depth security analysis of the behavior of weight-space classifiers under adversarial attacks. Our study reveals that parameter-space models trained for classification exhibit increased robustness to standard white-box adversarial attacks compared to standard classifiers that operate in the original signal space. This is achieved without the need of any robust training. We source this robust behavior to the phenomenon of gradient-obfuscation promoted during the INR optimization process, and pinpoint the limitations of this robustness under alternative adversarial approaches. To support our claims, we develop a novel suite of adversarial attacks targeting parameter-space classifiers, and furthermore analyze practical considerations of such attacks.
</details>

---


### [Weight Space Representation Learning on Diverse NeRF Architectures](https://arxiv.org/abs/2502.09623)
**Authors:** Ballerini, Francesco and Ramirez, Pierluigi Zama and Stefano, Luigi Di and Salti, Samuele  
**Date:** 2025-02-13 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*International Conference on Learning Representations* · 2025 · [arXiv:2502.09623](https://arxiv.org/abs/2502.09623)

<details>
<summary>Abstract</summary>

> Neural Radiance Fields (NeRFs) have emerged as a groundbreaking paradigm for representing 3D objects and scenes by encoding shape and appearance information into the weights of a neural network. Recent studies have demonstrated that these weights can be used as input for frameworks designed to address deep learning tasks; however, such frameworks require NeRFs to adhere to a specific, predefined architecture. In this paper, we introduce the first framework capable of processing NeRFs with diverse architectures and performing inference on architectures unseen at training time. We achieve this by training a Graph Meta-Network within an unsupervised representation learning framework, and show that a contrastive objective is conducive to obtaining an architecture-agnostic latent space. In experiments conducted across 13 NeRF architectures belonging to three families (MLPs, tri-planes, and, for the first time, hash tables), our approach demonstrates robust performance in classification, retrieval, and language tasks involving multiple architectures, even unseen at training time, while also matching or exceeding the results of existing frameworks limited to single architectures. Our code and data are available at https://cvlab-unibo.github.io/gmnerf.
</details>

---


### [Can this Model Also Recognize Dogs? Zero-Shot Model Search from Weights](https://arxiv.org/abs/2502.09619)
**Authors:** Kahana, Jonathan and Nathan, Or and Horwitz, Eliahu and Hoshen, Yedid  
**Date:** 2025-02-13 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2025 · [arXiv:2502.09619](https://arxiv.org/abs/2502.09619)

<details>
<summary>Abstract</summary>

> With the increasing numbers of publicly available models, there are probably pretrained, online models for most tasks users require. However, current model search methods are rudimentary, essentially a text-based search in the documentation, thus users cannot find the relevant models. This paper presents ProbeLog, a method for retrieving classification models that can recognize a target concept, such as "Dog", without access to model metadata or training data. Differently from previous probing methods, ProbeLog computes a descriptor for each output dimension (logit) of each model, by observing its responses on a fixed set of inputs (probes). Our method supports both logit-based retrieval ("find more logits like this") and zero-shot, text-based retrieval ("find all logits corresponding to dogs"). As probing-based representations require multiple costly feedforward passes through the model, we develop a method, based on collaborative filtering, that reduces the cost of encoding repositories by 3x. We demonstrate that ProbeLog achieves high retrieval accuracy, both in real-world and fine-grained search tasks and is scalable to full-size repositories.
</details>

---


### [Weight Space Learning for Certifiable Few-shot Transfer Learning](https://arxiv.org/abs/2502.06970)
**Authors:** Rezk, Fady and Lee, Royson and Gouk, Henry and Hospedales, Timothy and Kim, Minyoung  
**Date:** 2025-02-10 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2025 · [arXiv:2502.06970](https://arxiv.org/abs/2502.06970)

<details>
<summary>Abstract</summary>

> In contemporary deep learning, a prevalent and effective workflow for solving low-data problems is adapting powerful pre-trained foundation models (FMs) to new tasks via parameter-efficient fine-tuning (PEFT). However, while empirically effective, the resulting solutions lack generalisation guarantees to certify their accuracy - which may be required for ethical or legal reasons prior to deployment in high-importance applications. In this paper we develop a novel transfer learning approach that is designed to facilitate non-vacuous learning theoretic generalisation guarantees for downstream tasks, even in the low-shot regime. Specifically, we first use upstream tasks to train a distribution over PEFT parameters. We then learn the downstream task by a sample-and-evaluate procedure -- sampling plausible PEFTs from the trained diffusion model and selecting the one with the highest likelihood on the downstream data. Crucially, this confines our model hypothesis to a finite set of PEFT samples. In contrast to the typical continuous hypothesis spaces of neural network weights, this facilitates tighter risk certificates. We instantiate our bound and show non-trivial generalization guarantees compared to existing learning approaches which lead to vacuous bounds in the low-shot regime.
</details>

---


### [Beyond the Permutation Symmetry of Transformers: The Role of Rotation for Model Fusion](https://arxiv.org/abs/2502.00264)
**Authors:** Zhang, Binchi and Zheng, Zaiyi and Chen, Zhengzhang and Li, Jundong  
**Date:** 2025-02-01 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2025 · [arXiv:2502.00264](https://arxiv.org/abs/2502.00264)

<details>
<summary>Abstract</summary>

> Symmetry in the parameter space of deep neural networks (DNNs) has proven beneficial for various deep learning applications. A well-known example is the permutation symmetry in Multi-Layer Perceptrons (MLPs), where permuting the rows of weight matrices in one layer and applying the inverse permutation to adjacent layers yields a functionally equivalent model. While permutation symmetry fully characterizes the equivalence set for MLPs, its discrete nature limits its utility for transformers. In this paper, we introduce rotation symmetry, a novel form of parameter space symmetry for transformers that generalizes permutation symmetry by rotating parameter matrices in self-attention layers. Unlike permutation symmetry, rotation symmetry operates in a continuous domain, thereby significantly expanding the equivalence set for transformers. Based on this property, we propose a theoretically optimal parameter matching algorithm as a plug-and-play module to enhance model fusion. We evaluate our approach using pre-trained transformers across diverse natural language and vision tasks. Experimental results demonstrate that our rotation symmetry-based matching algorithm substantially improves model fusion, highlighting the potential of parameter space symmetry to facilitate model fusion. Our code is available on https://github.com/zhengzaiyi/RotationSymmetry.
</details>

---


### [Large-Scale Riemannian Meta-Optimization via Subspace Adaptation](https://arxiv.org/abs/2501.15235)
**Authors:** Yu, Peilin and Wu, Yuwei and Gao, Zhi and Fan, Xiaomeng and Jia, Yunde  
**Date:** 2025-01-25 · **Topics:** General-Purpose Learned Optimizers  
*Computer Vision and Image Understanding* · 2025 · [arXiv:2501.15235](https://arxiv.org/abs/2501.15235)

<details>
<summary>Abstract</summary>

> Riemannian meta-optimization provides a promising approach to solving non-linear constrained optimization problems, which trains neural networks as optimizers to perform optimization on Riemannian manifolds. However, existing Riemannian meta-optimization methods take up huge memory footprints in large-scale optimization settings, as the learned optimizer can only adapt gradients of a fixed size and thus cannot be shared across different Riemannian parameters. In this paper, we propose an efficient Riemannian meta-optimization method that significantly reduces the memory burden for large-scale optimization via a subspace adaptation scheme. Our method trains neural networks to individually adapt the row and column subspaces of Riemannian gradients, instead of directly adapting the full gradient matrices in existing Riemannian meta-optimization methods. In this case, our learned optimizer can be shared across Riemannian parameters with different sizes. Our method reduces the model memory consumption by six orders of magnitude when optimizing an orthogonal mainstream deep neural network (e.g., ResNet50). Experiments on multiple Riemannian tasks show that our method can not only reduce the memory consumption but also improve the performance of Riemannian meta-optimization.
</details>

---


### [Celo: Training Versatile Learned Optimizers on a Compute Diet](https://www.semanticscholar.org/paper/3fd5e6f90f34109f8737cb307d29d08a3638bd24)
**Authors:** Moudgil, Abhinav and Knyazev, Boris and Lajoie, Guillaume and Belilovsky, Eugene  
**Date:** 2025-01-22 · **Topics:** General-Purpose Learned Optimizers  
*Trans. Mach. Learn. Res.* · 2025 · [arXiv:2501.12670](https://arxiv.org/abs/2501.12670)

<details>
<summary>Abstract</summary>

> Learned optimization has emerged as a promising alternative to hand-crafted optimizers, with the potential to discover stronger learned update rules that enable faster, hyperparameter-free training of neural networks. A critical element for practically useful learned optimizers, that can be used off-the-shelf after meta-training, is strong meta-generalization: the ability to apply the optimizers to new tasks. Recent state-of-the-art work in learned optimizers, VeLO (Metz et al., 2022), requires a large number of highly diverse meta-training tasks along with massive computational resources, 4000 TPU months, to achieve meta-generalization. This makes further improvements to such learned optimizers impractical. In this work, we identify several key elements in learned optimizer architectures and meta-training procedures that can lead to strong meta-generalization. We also propose evaluation metrics to reliably assess quantitative performance of an optimizer at scale on a set of evaluation tasks. Our proposed approach, Celo, makes a significant leap in improving the meta-generalization performance of learned optimizers and also outperforms tuned state-of-the-art optimizers on a diverse set of out-of-distribution tasks, despite being meta-trained for just 24 GPU hours.
</details>

---


## 2024

### [Learning to Generate Gradients for Test-Time Adaptation via Test-Time Training Layers](https://arxiv.org/abs/2412.16901)
**Authors:** Deng, Qi and Niu, Shuaicheng and Zhang, Ronghao and Chen, Yaofo and Zeng, Runhao and Chen, Jian and Hu, Xiping  
**Date:** 2024-12-22 · **Topics:** Learned Optimizers in Specific Domains  
*AAAI 2025* · 2024 · [arXiv:2412.16901](https://arxiv.org/abs/2412.16901)

<details>
<summary>Abstract</summary>

> Test-time adaptation (TTA) aims to fine-tune a trained model online using unlabeled testing data to adapt to new environments or out-of-distribution data, demonstrating broad application potential in real-world scenarios. However, in this optimization process, unsupervised learning objectives like entropy minimization frequently encounter noisy learning signals. These signals produce unreliable gradients, which hinder the model ability to converge to an optimal solution quickly and introduce significant instability into the optimization process. In this paper, we seek to resolve these issues from the perspective of optimizer design. Unlike prior TTA using manually designed optimizers like SGD, we employ a learning-to-optimize approach to automatically learn an optimizer, called Meta Gradient Generator (MGG). Specifically, we aim for MGG to effectively utilize historical gradient information during the online optimization process to optimize the current model. To this end, in MGG, we design a lightweight and efficient sequence modeling layer -- gradient memory layer. It exploits a self-supervised reconstruction loss to compress historical gradient information into network parameters, thereby enabling better memorization ability over a long-term adaptation process. We only need a small number of unlabeled samples to pre-train MGG, and then the trained MGG can be deployed to process unseen samples. Promising results on ImageNet-C, R, Sketch, and A indicate that our method surpasses current state-of-the-art methods with fewer updates, less data, and significantly shorter adaptation iterations. Compared with a previous SOTA method SAR, we achieve 7.4% accuracy improvement and 4.2 times faster adaptation speed on ImageNet-C.
</details>

---


### [Learning on Model Weights using Tree Experts](https://arxiv.org/abs/2410.13569)
**Authors:** Horwitz, Eliahu and Cavia, Bar and Kahana, Jonathan and Hoshen, Yedid  
**Date:** 2024-10-17 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*IEEE Computer Society Conference on Computer Vision and Pattern Recognition/Proceedings - IEEE Computer Society Conference on Computer Vision and Pattern Recognition/Proceedings* · 2024 · [arXiv:2410.13569](https://arxiv.org/abs/2410.13569)

<details>
<summary>Abstract</summary>

> The number of publicly available models is rapidly increasing, yet most remain undocumented. Users looking for suitable models for their tasks must first determine what each model does. Training machine learning models to infer missing documentation directly from model weights is challenging, as these weights often contain significant variation unrelated to model functionality (denoted nuisance). Here, we identify a key property of real-world models: most public models belong to a small set of Model Trees, where all models within a tree are fine-tuned from a common ancestor (e.g., a foundation model). Importantly, we find that within each tree there is less nuisance variation between models. Concretely, while learning across Model Trees requires complex architectures, even a linear classifier trained on a single model layer often works within trees. While effective, these linear classifiers are computationally expensive, especially when dealing with larger models that have many parameters. To address this, we introduce Probing Experts (ProbeX), a theoretically motivated and lightweight method. Notably, ProbeX is the first probing method specifically designed to learn from the weights of a single hidden model layer. We demonstrate the effectiveness of ProbeX by predicting the categories in a model's training dataset based only on its weights. Excitingly, ProbeX can map the weights of Stable Diffusion into a weight-language embedding space, enabling model search via text, i.e., zero-shot model classification.
</details>

---


### [Deep Linear Probe Generators for Weight Space Learning](https://arxiv.org/abs/2410.10811)
**Authors:** Kahana, Jonathan and Horwitz, Eliahu and Shuval, Imri and Hoshen, Yedid  
**Date:** 2024-10-14 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*International Conference on Learning Representations* · 2024 · [arXiv:2410.10811](https://arxiv.org/abs/2410.10811)

<details>
<summary>Abstract</summary>

> Weight space learning aims to extract information about a neural network, such as its training dataset or generalization error. Recent approaches learn directly from model weights, but this presents many challenges as weights are high-dimensional and include permutation symmetries between neurons. An alternative approach, Probing, represents a model by passing a set of learned inputs (probes) through the model, and training a predictor on top of the corresponding outputs. Although probing is typically not used as a stand alone approach, our preliminary experiment found that a vanilla probing baseline worked surprisingly well. However, we discover that current probe learning strategies are ineffective. We therefore propose Deep Linear Probe Generators (ProbeGen), a simple and effective modification to probing approaches. ProbeGen adds a shared generator module with a deep linear architecture, providing an inductive bias towards structured probes thus reducing overfitting. While simple, ProbeGen performs significantly better than the state-of-the-art and is very efficient, requiring between 30 to 1000 times fewer FLOPs than other top approaches.
</details>

---


### [Revisiting Multi-Permutation Equivariance through the Lens of Irreducible Representations](https://arxiv.org/abs/2410.06665)
**Authors:** Sverdlov, Yonatan and Springer, Ido and Dym, Nadav  
**Date:** 2024-10-09 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*International Conference on Learning Representations* · 2024 · [arXiv:2410.06665](https://arxiv.org/abs/2410.06665)

<details>
<summary>Abstract</summary>

> This paper explores the characterization of equivariant linear layers for representations of permutations and related groups. Unlike traditional approaches, which address these problems using parameter-sharing, we consider an alternative methodology based on irreducible representations and Schur's lemma. Using this methodology, we obtain an alternative derivation for existing models like DeepSets, 2-IGN graph equivariant networks, and Deep Weight Space (DWS) networks. The derivation for DWS networks is significantly simpler than that of previous results. Next, we extend our approach to unaligned symmetric sets, where equivariance to the wreath product of groups is required. Previous works have addressed this problem in a rather restrictive setting, in which almost all wreath equivariant layers are Siamese. In contrast, we give a full characterization of layers in this case and show that there is a vast number of additional non-Siamese layers in some settings. We also show empirically that these additional non-Siamese layers can improve performance in tasks like graph anomaly detection, weight space alignment, and learning Wasserstein distances. Our code is available at \hrefhttps://github.com/yonatansverdlov/Irreducible-Representations-of-Deep-Weight-SpacesGitHub.
</details>

---


### [Equivariant Neural Functional Networks for Transformers](https://arxiv.org/abs/2410.04209)
**Authors:** Tran, Viet-Hoang and Vo, Thieu N. and The, An Nguyen and Huu, Tho Tran and Nguyen-Nhat, Minh-Khoi and Tran, Thanh and Pham, Duy-Tung and Nguyen, Tan Minh  
**Date:** 2024-10-05 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*International Conference on Learning Representations* · 2024 · [arXiv:2410.04209](https://arxiv.org/abs/2410.04209)

<details>
<summary>Abstract</summary>

> This paper systematically explores neural functional networks (NFN) for transformer architectures. NFN are specialized neural networks that treat the weights, gradients, or sparsity patterns of a deep neural network (DNN) as input data and have proven valuable for tasks such as learnable optimizers, implicit data representations, and weight editing. While NFN have been extensively developed for MLP and CNN, no prior work has addressed their design for transformers, despite the importance of transformers in modern deep learning. This paper aims to address this gap by providing a systematic study of NFN for transformers. We first determine the maximal symmetric group of the weights in a multi-head attention module as well as a necessary and sufficient condition under which two sets of hyperparameters of the multi-head attention module define the same function. We then define the weight space of transformer architectures and its associated group action, which leads to the design principles for NFN in transformers. Based on these, we introduce Transformer-NFN, an NFN that is equivariant under this group action. Additionally, we release a dataset of more than 125,000 Transformers model checkpoints trained on two datasets with two different tasks, providing a benchmark for evaluating Transformer-NFN and encouraging further research on transformer training and performance.
</details>

---


### [Accelerating Training with Neuron Interaction and Nowcasting Networks](https://arxiv.org/abs/2409.04434) — 🔗 *LO-linked*
**Authors:** Knyazev, Boris and Moudgil, Abhinav and Lajoie, Guillaume and Belilovsky, Eugene and Lacoste-Julien, Simon  
**Date:** 2024-09-06 · **Topics:** General-Purpose Learned Optimizers, Weight-Space Learning & Graph Metanetworks  
*International Conference on Learning Representations* · 2024 · [arXiv:2409.04434](https://arxiv.org/abs/2409.04434)

<details>
<summary>Abstract</summary>

> Neural network training can be accelerated when a learnable update rule is used in lieu of classic adaptive optimizers (e.g. Adam). However, learnable update rules can be costly and unstable to train and use. Recently, Jang et al. (2023) proposed a simpler approach to accelerate training based on weight nowcaster networks (WNNs). In their approach, Adam is used for most of the optimization steps and periodically, only every few steps, a WNN nowcasts (predicts near future) parameters. We improve WNNs by proposing neuron interaction and nowcasting (NiNo) networks. In contrast to WNNs, NiNo leverages neuron connectivity and graph neural networks to more accurately nowcast parameters. We further show that in some networks, such as Transformers, modeling neuron connectivity accurately is challenging. We address this and other limitations, which allows NiNo to accelerate Adam training by up to 50% in vision and language tasks.
</details>

---


### [Can Learned Optimization Make Reinforcement Learning Less Difficult?](https://www.semanticscholar.org/paper/5ecf53ab083f72f10421225a7dde25eb51cb6b22)
**Authors:** Goldie, Alexander David and Lu, Chris Xiaoxuan and Jackson, Matthew Thomas and Whiteson, Shimon and Foerster, Jakob  
**Date:** 2024-07-09 · **Topics:** Learned Optimizers in Specific Domains  
*arXiv.org* · 2024 · [arXiv:2407.07082](https://arxiv.org/abs/2407.07082)

<details>
<summary>Abstract</summary>

> While reinforcement learning (RL) holds great potential for decision making in the real world, it suffers from a number of unique difficulties which often need specific consideration. In particular: it is highly non-stationary; suffers from high degrees of plasticity loss; and requires exploration to prevent premature convergence to local optima and maximize return. In this paper, we consider whether learned optimization can help overcome these problems. Our method, Learned Optimization for Plasticity, Exploration and Non-stationarity (OPEN), meta-learns an update rule whose input features and output structure are informed by previously proposed solutions to these difficulties. We show that our parameterization is flexible enough to enable meta-learning in diverse learning contexts, including the ability to use stochasticity for exploration. Our experiments demonstrate that when meta-trained on single and small sets of environments, OPEN outperforms or equals traditionally used optimizers. Furthermore, OPEN shows strong generalization characteristics across a range of environments and agent architectures.
</details>

---


### [Improving Hyperparameter Optimization with Checkpointed Model Weights](https://arxiv.org/abs/2406.18630)
**Authors:** Mehta, Nikhil and Lorraine, Jonathan and Masson, Steve and Arunachalam, Ramanathan and Bhat, Zaid Pervaiz and Lucas, James and Zachariah, Arun George  
**Date:** 2024-06-26 · **Topics:** Related Meta-Learning & Hyperparameter Adaptation, Weight-Space Learning & Graph Metanetworks  
*Lecture notes in computer science* · 2024 · [arXiv:2406.18630](https://arxiv.org/abs/2406.18630)

<details>
<summary>Abstract</summary>

> When training deep learning models, the performance depends largely on the selected hyperparameters. However, hyperparameter optimization (HPO) is often one of the most expensive parts of model design. Classical HPO methods treat this as a black-box optimization problem. However, gray-box HPO methods, which incorporate more information about the setup, have emerged as a promising direction for more efficient optimization. For example, using intermediate loss evaluations to terminate bad selections. In this work, we propose an HPO method for neural networks using logged checkpoints of the trained weights to guide future hyperparameter selections. Our method, Forecasting Model Search (FMS), embeds weights into a Gaussian process deep kernel surrogate model, using a permutation-invariant graph metanetwork to be data-efficient with the logged network weights. To facilitate reproducibility and further research, we open-source our code at https://github.com/NVlabs/forecasting-model-search.
</details>

---


### [Scale Equivariant Graph Metanetworks](https://www.semanticscholar.org/paper/d584110aad0ba7492823d041b18af4ca77239c95)
**Authors:** Kalogeropoulos, Ioannis and Bouritsas, Giorgos and Panagakis, Yannis  
**Date:** 2024-06-15 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv.org* · 2024 · [arXiv:2406.10685](https://arxiv.org/abs/2406.10685)

<details>
<summary>Abstract</summary>

> This paper pertains to an emerging machine learning paradigm: learning higher-order functions, i.e. functions whose inputs are functions themselves, $\textitparticularly when these inputs are Neural Networks (NNs)$. With the growing interest in architectures that process NNs, a recurring design principle has permeated the field: adhering to the permutation symmetries arising from the connectionist structure of NNs. $\textitHowever, are these the sole symmetries present in NN parameterizations$? Zooming into most practical activation functions (e.g. sine, ReLU, tanh) answers this question negatively and gives rise to intriguing new symmetries, which we collectively refer to as $\textitscaling symmetries$, that is, non-zero scalar multiplications and divisions of weights and biases. In this work, we propose $\textitScale Equivariant Graph MetaNetworks - ScaleGMNs$, a framework that adapts the Graph Metanetwork (message-passing) paradigm by incorporating scaling symmetries and thus rendering neuron and edge representations equivariant to valid scalings. We introduce novel building blocks, of independent technical interest, that allow for equivariance or invariance with respect to individual scalar multipliers or their product and use them in all components of ScaleGMN. Furthermore, we prove that, under certain expressivity conditions, ScaleGMN can simulate the forward and backward pass of any input feedforward neural network. Experimental results demonstrate that our method advances the state-of-the-art performance for several datasets and activation functions, highlighting the power of scaling symmetries as an inductive bias for NN processing. The source code is publicly available at https://github.com/jkalogero/scalegmn.
</details>

---


### [μLO: Compute-Efficient Meta-Generalization of Learned Optimizers](https://www.semanticscholar.org/paper/7cb61bf31a57366343b323f554e71be35ee83b91)
**Authors:** Thérien, Benjamin and Joseph, C. and Knyazev, B. A. and Oyallon, Edouard and Rish, Irina and Belilovsky, Eugene  
**Date:** 2024-05-31 · **Topics:** General-Purpose Learned Optimizers  
*arXiv.org* · 2024 · [arXiv:2406.00153](https://arxiv.org/abs/2406.00153)

<details>
<summary>Abstract</summary>

> Learned optimizers (LOs) have the potential to significantly reduce the wall-clock training time of neural networks. However, they can struggle to optimize unseen tasks (\emphmeta-generalize), especially when training networks wider than those seen during meta-training. To address this, we derive the Maximal Update Parametrization ($\mu$P) for two state-of-the-art learned optimizer architectures and propose a simple meta-training recipe for $\mu$-parameterized LOs ($\mu$LOs). Our empirical evaluation demonstrates that LOs meta-trained with our recipe substantially improve meta-generalization to wider unseen tasks when compared to LOs trained under standard parametrization (SP) using the same compute budget. We also empirically observe that $\mu$LOs exhibit unexpectedly improved meta-generalization to deeper networks ($5\times$ meta-training) and surprising generalization to much longer training horizons ($25\times$ meta-training) when compared to SP LOs.
</details>

---


### [Unsupervised Model Tree Heritage Recovery](https://arxiv.org/abs/2405.18432)
**Authors:** Horwitz, Eliahu and Shul, Asaf and Hoshen, Yedid  
**Date:** 2024-05-28 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*International Conference on Learning Representations* · 2024 · [arXiv:2405.18432](https://arxiv.org/abs/2405.18432)

<details>
<summary>Abstract</summary>

> The number of models shared online has recently skyrocketed, with over one million public models available on Hugging Face. Sharing models allows other users to build on existing models, using them as initialization for fine-tuning, improving accuracy, and saving compute and energy. However, it also raises important intellectual property issues, as fine-tuning may violate the license terms of the original model or that of its training data. A Model Tree, i.e., a tree data structure rooted at a foundation model and having directed edges between a parent model and other models directly fine-tuned from it (children), would settle such disputes by making the model heritage explicit. Unfortunately, current models are not well documented, with most model metadata (e.g., "model cards") not providing accurate information about heritage. In this paper, we introduce the task of Unsupervised Model Tree Heritage Recovery (Unsupervised MoTHer Recovery) for collections of neural networks. For each pair of models, this task requires: i) determining if they are directly related, and ii) establishing the direction of the relationship. Our hypothesis is that model weights encode this information, the challenge is to decode the underlying tree structure given the weights. We discover several properties of model weights that allow us to perform this task. By using these properties, we formulate the MoTHer Recovery task as finding a directed minimal spanning tree. In extensive experiments we demonstrate that our method successfully reconstructs complex Model Trees.
</details>

---


### [Graph Neural Networks for Learning Equivariant Representations of Neural Networks](https://www.semanticscholar.org/paper/fc580c211689663a64f42e2ba92c864cb134ba9b) — 🔗 *LO-linked*
**Authors:** Kofinas, Miltiadis and Knyazev, Boris and Zhang, Yan and Chen, Yunlu and Burghouts, Gertjan J. and Gavves, Efstratios and Snoek, Cees G. M. and Zhang, David  
**Date:** 2024-03-18 · **Topics:** Weight-Space Learning & Graph Metanetworks, General-Purpose Learned Optimizers  
*arXiv.org* · 2024 · [arXiv:2403.12143](https://arxiv.org/abs/2403.12143)

<details>
<summary>Abstract</summary>

> Neural networks that process the parameters of other neural networks find applications in domains as diverse as classifying implicit neural representations, generating neural network weights, and predicting generalization errors. However, existing approaches either overlook the inherent permutation symmetry in the neural network or rely on intricate weight-sharing patterns to achieve equivariance, while ignoring the impact of the network architecture itself. In this work, we propose to represent neural networks as computational graphs of parameters, which allows us to harness powerful graph neural networks and transformers that preserve permutation symmetry. Consequently, our approach enables a single model to encode neural computational graphs with diverse architectures. We showcase the effectiveness of our method on a wide range of tasks, including classification and editing of implicit neural representations, predicting generalization performance, and learning to optimize, while consistently outperforming state-of-the-art methods. The source code is open-sourced at https://github.com/mkofinas/neural-graphs.
</details>

---


### [Moco: A Learnable Meta Optimizer for Combinatorial Optimization](https://arxiv.org/abs/2402.04915)
**Authors:** Dernedde, Tim and Thyssens, Daniela and Dittrich, Sören and Stubbemann, Maximilian and Schmidt-Thieme, Lars  
**Date:** 2024-02-07 · **Topics:** Learned Optimizers in Specific Domains  
*Lecture notes in computer science* · 2024 · [arXiv:2402.04915](https://arxiv.org/abs/2402.04915)

<details>
<summary>Abstract</summary>

> Relevant combinatorial optimization problems (COPs) are often NP-hard. While they have been tackled mainly via handcrafted heuristics in the past, advances in neural networks have motivated the development of general methods to learn heuristics from data. Many approaches utilize a neural network to directly construct a solution, but are limited in further improving based on already constructed solutions at inference time. Our approach, Moco, defines a lightweight solution construction procedure, guided by a single continuous vector $θ$ (called heatmap) and learns a neural network to update $θ$ for a single instance of a COP at inference time. The update is based on various features of the current search state. The training procedure is budget aware, targeting the overall best solution found during the entire search. Moco is a fully learnable meta optimizer not utilizing problem specific heuristics or requiring optimal solutions for training. We test Moco on the Traveling Salesman Problem (TSP) and Maximum Independent Set (MIS) and show that it significantly improves over other heatmap based methods.
</details>

---


### [MADA: Meta-Adaptive Optimizers through hyper-gradient Descent](https://www.semanticscholar.org/paper/bef33d15c3e8d433261f97f7001cc41a5ae0ec32)
**Authors:** Ozkara, Kaan and Karakus, Can and Raman, Parameswaran and Hong, Mingyi and Sabach, Shoham and Kveton, Branislav and Cevher, Volkan  
**Date:** 2024-01-17 · **Topics:** Related Meta-Learning & Hyperparameter Adaptation  
*arXiv.org* · 2024 · [arXiv:2401.08893](https://arxiv.org/abs/2401.08893)

<details>
<summary>Abstract</summary>

> Following the introduction of Adam, several novel adaptive optimizers for deep learning have been proposed. These optimizers typically excel in some tasks but may not outperform Adam uniformly across all tasks. In this work, we introduce Meta-Adaptive Optimizers (MADA), a unified optimizer framework that can generalize several known optimizers and dynamically learn the most suitable one during training. The key idea in MADA is to parameterize the space of optimizers and dynamically search through it using hyper-gradient descent during training. We empirically compare MADA to other popular optimizers on vision and language tasks, and find that MADA consistently outperforms Adam and other popular optimizers, and is robust against sub-optimally tuned hyper-parameters. MADA achieves a greater validation performance improvement over Adam compared to other popular optimizers during GPT-2 training and fine-tuning. We also propose AVGrad, a modification of AMSGrad that replaces the maximum operator with averaging, which is more suitable for hyper-gradient optimization. Finally, we provide a convergence analysis to show that parameterized interpolations of optimizers can improve their error bounds (up to constants), hinting at an advantage for meta-optimizers.
</details>

---


## 2023

### [Graph Metanetworks for Processing Diverse Neural Architectures](https://www.semanticscholar.org/paper/af8df99efea4d4ed6f5cf6f6eaf3a5943f4d75db)
**Authors:** Lim, Derek and Maron, Haggai and Law, Marc T. and Lorraine, Jonathan and Lucas, James M.  
**Date:** 2023-12-07 · **Topics:** Weight-Space Learning & Graph Metanetworks  
*arXiv (Cornell University)* · 2023 · [arXiv:2312.04501](https://arxiv.org/abs/2312.04501)

<details>
<summary>Abstract</summary>

> Neural networks efficiently encode learned information within their parameters. Consequently, many tasks can be unified by treating neural networks themselves as input data. When doing so, recent studies demonstrated the importance of accounting for the symmetries and geometry of parameter spaces. However, those works developed architectures tailored to specific networks such as MLPs and CNNs without normalization layers, and generalizing such architectures to other types of networks can be challenging. In this work, we overcome these challenges by building new metanetworks - neural networks that take weights from other neural networks as input. Put simply, we carefully build graphs representing the input neural networks and process the graphs using graph neural networks. Our approach, Graph Metanetworks (GMNs), generalizes to neural architectures where competing methods struggle, such as multi-head attention layers, normalization layers, convolutional layers, ResNet blocks, and group-equivariant linear layers. We prove that GMNs are expressive and equivariant to parameter permutation symmetries that leave the input neural network functions unchanged. We validate the effectiveness of our method on several metanetwork tasks over diverse neural network architectures.
</details>

---


### [Meta-learning Optimizers for Communication-Efficient Learning](https://www.semanticscholar.org/paper/4ff9ae519bd9084af922479955b53674afcdb3fb)
**Authors:** Charles-'Etienne Joseph  
**Date:** 2023-12-02 · **Topics:** Learned Optimizers in Specific Domains  
*Trans. Mach. Learn. Res.* · 2023 · [arXiv:2312.02204](https://arxiv.org/abs/2312.02204)

<details>
<summary>Abstract</summary>

> Communication-efficient variants of SGD, specifically local SGD, have received a great deal of interest in recent years. These approaches compute multiple gradient steps locally on each worker, before averaging model parameters, helping relieve the critical communication bottleneck in distributed deep learning training. Although many variants of these approaches have been proposed, they can sometimes lag behind state-of-the-art adaptive optimizers for deep learning. In this work, we investigate if the recent progress in the emerging area of learned optimizers can potentially close this gap in homogeneous data and homogeneous device settings while remaining communication-efficient. Specifically, we meta-learn how to perform global updates given an update from local SGD iterations. Our results demonstrate that learned optimizers can substantially outperform local SGD and its sophisticated variants while maintaining their communication efficiency. Our learned optimizers can even generalize to unseen and much larger datasets and architectures, including ImageNet and ViTs, and to unseen modalities such as language modeling. We therefore show the potential of learned optimizers for improving communication-efficient distributed learning.
</details>

---


### [Is Scaling Learned Optimizers Worth It? Evaluating The Value of VeLO's 4000 TPU Months](https://www.semanticscholar.org/paper/d92fe2b8861e8ef74e030d674bedcd505a98def9)
**Authors:** Antoniou, Antreas and Gouk, Henry and Hospedales, Timothy M.  
**Date:** 2023-10-27 · **Topics:** General-Purpose Learned Optimizers  
*ICBINB* · 2023 · [arXiv:2310.18191](https://arxiv.org/abs/2310.18191)

<details>
<summary>Abstract</summary>

> We analyze VeLO (versatile learned optimizer), the largest scale attempt to train a general purpose"foundational"optimizer to date. VeLO was trained on thousands of machine learning tasks using over 4000 TPU months with the goal of producing an optimizer capable of generalizing to new problems while being hyperparameter free, and outperforming industry standards such as Adam. We independently evaluate VeLO on the MLCommons optimizer benchmark suite. We find that, contrary to initial claims: (1) VeLO has a critical hyperparameter that needs problem-specific tuning, (2) VeLO does not necessarily outperform competitors in quality of solution found, and (3) VeLO is not faster than competing optimizers at reducing the training loss. These observations call into question VeLO's generality and the value of the investment in training it.
</details>

---


### [B2Opt: Learning to Optimize Black-box Optimization with Little Budget](https://arxiv.org/abs/2304.11787)
**Authors:** Li, Xiaobin and Wu, Kai and Zhang, Xiaoyu and Wang, Handing and Liu, Jing  
**Date:** 2023-04-24 · **Topics:** Learned Optimizers in Specific Domains  
*Proceedings of the AAAI Conference on Artificial Intelligence* · 2023 · [arXiv:2304.11787](https://arxiv.org/abs/2304.11787)

<details>
<summary>Abstract</summary>

> The core challenge of high-dimensional and expensive black-box optimization (BBO) is how to obtain better performance faster with little function evaluation cost. The essence of the problem is how to design an efficient optimization strategy tailored to the target task. This paper designs a powerful optimization framework to automatically learn the optimization strategies from the target or cheap surrogate task without human intervention. However, current methods are weak for this due to poor representation of optimization strategy. To achieve this, 1) drawing on the mechanism of genetic algorithm, we propose a deep neural network framework called B2Opt, which has a stronger representation of optimization strategies based on survival of the fittest; 2) B2Opt can utilize the cheap surrogate functions of the target task to guide the design of the efficient optimization strategies. Compared to the state-of-the-art BBO baselines, B2Opt can achieve multiple orders of magnitude performance improvement with less function evaluation cost. We validate our proposal on high-dimensional synthetic functions and two real-world applications. We also find that deep B2Opt performs better than shallow ones.
</details>

---


### [Improving physics-informed neural networks with meta-learned optimization](https://www.semanticscholar.org/paper/4f9f96679e943f7447ac431dffea506767d3cf3f)
**Authors:** Bihlo, Alex  
**Date:** 2023-03-13 · **Topics:** Learned Optimizers in Specific Domains  
*arXiv (Cornell University)* · 2023 · [arXiv:2303.07127](https://arxiv.org/abs/2303.07127)

<details>
<summary>Abstract</summary>

> We show that the error achievable using physics-informed neural networks for solving systems of differential equations can be substantially reduced when these networks are trained using meta-learned optimization methods rather than to using fixed, hand-crafted optimizers as traditionally done. We choose a learnable optimization method based on a shallow multi-layer perceptron that is meta-trained for specific classes of differential equations. We illustrate meta-trained optimizers for several equations of practical relevance in mathematical physics, including the linear advection equation, Poisson's equation, the Korteweg--de Vries equation and Burgers' equation. We also illustrate that meta-learned optimizers exhibit transfer learning abilities, in that a meta-trained optimizer on one differential equation can also be successfully deployed on another differential equation.
</details>

---


### [Learning to Generalize Provably in Learning to Optimize](https://arxiv.org/abs/2302.11085)
**Authors:** Yang, Junjie and Chen, Tianlong and Zhu, Mingkang and He, Fengxiang and Tao, Dacheng and Liang, Yingbin and Wang, Zhangyang  
**Date:** 2023-02-22 · **Topics:** General-Purpose Learned Optimizers  
*International Conference on Artificial Intelligence and Statistics* · 2023 · [arXiv:2302.11085](https://arxiv.org/abs/2302.11085)

<details>
<summary>Abstract</summary>

> Learning to optimize (L2O) has gained increasing popularity, which automates the design of optimizers by data-driven approaches. However, current L2O methods often suffer from poor generalization performance in at least two folds: (i) applying the L2O-learned optimizer to unseen optimizees, in terms of lowering their loss function values (optimizer generalization, or ``generalizable learning of optimizers"); and (ii) the test performance of an optimizee (itself as a machine learning model), trained by the optimizer, in terms of the accuracy over unseen data (optimizee generalization, or ``learning to generalize"). While the optimizer generalization has been recently studied, the optimizee generalization (or learning to generalize) has not been rigorously studied in the L2O context, which is the aim of this paper. We first theoretically establish an implicit connection between the local entropy and the Hessian, and hence unify their roles in the handcrafted design of generalizable optimizers as equivalent metrics of the landscape flatness of loss functions. We then propose to incorporate these two metrics as flatness-aware regularizers into the L2O framework in order to meta-train optimizers to learn to generalize, and theoretically show that such generalization ability can be learned during the L2O meta-training process and then transformed to the optimizee loss function. Extensive experiments consistently validate the effectiveness of our proposals with substantially improved generalization on multiple sophisticated L2O models and diverse optimizees. Our code is available at: https://github.com/VITA-Group/Open-L2O/tree/main/Model_Free_L2O/L2O-Entropy.
</details>

---


## 2022

### [VeLO: Training Versatile Learned Optimizers by Scaling Up](https://www.semanticscholar.org/paper/c088b46519c036149a9f6da4ec36383b800a0d2a)
**Authors:** Metz, Luke and Harrison, J. and Freeman, C. Daniel and Merchant, Amil and Beyer, Lucas and Bradbury, James T. and Agrawal, Naman and Poole, Ben and Mordatch, Igor and Roberts, Adam and Sohl‐Dickstein, Jascha  
**Date:** 2022-11-17 · **Topics:** General-Purpose Learned Optimizers  
*arXiv.org* · 2022 · [arXiv:2211.09760](https://arxiv.org/abs/2211.09760)

<details>
<summary>Abstract</summary>

> While deep learning models have replaced hand-designed features across many domains, these models are still trained with hand-designed optimizers. In this work, we leverage the same scaling approach behind the success of deep learning to learn versatile optimizers. We train an optimizer for deep learning which is itself a small neural network that ingests gradients and outputs parameter updates. Meta-trained with approximately four thousand TPU-months of compute on a wide variety of optimization tasks, our optimizer not only exhibits compelling performance, but optimizes in interesting and unexpected ways. It requires no hyperparameter tuning, instead automatically adapting to the specifics of the problem being optimized. We open source our learned optimizer, meta-training code, the associated train and test data, and an extensive optimizer benchmark suite with baselines at velo-code.github.io.
</details>

---


### [A Closer Look at Learned Optimization: Stability, Robustness, and Inductive Biases](https://www.semanticscholar.org/paper/2d59b386a6037a895edf72c4420b76f64d921ee4)
**Authors:** Harrison, J. and Metz, Luke and Sohl‐Dickstein, Jascha  
**Date:** 2022-09-22 · **Topics:** General-Purpose Learned Optimizers  
*Neural Information Processing Systems* · 2022 · [arXiv:2209.11208](https://arxiv.org/abs/2209.11208)

<details>
<summary>Abstract</summary>

> Learned optimizers -- neural networks that are trained to act as optimizers -- have the potential to dramatically accelerate training of machine learning models. However, even when meta-trained across thousands of tasks at huge computational expense, blackbox learned optimizers often struggle with stability and generalization when applied to tasks unlike those in their meta-training set. In this paper, we use tools from dynamical systems to investigate the inductive biases and stability properties of optimization algorithms, and apply the resulting insights to designing inductive biases for blackbox optimizers. Our investigation begins with a noisy quadratic model, where we characterize conditions in which optimization is stable, in terms of eigenvalues of the training dynamics. We then introduce simple modifications to a learned optimizer's architecture and meta-training procedure which lead to improved stability, and improve the optimizer's inductive bias. We apply the resulting learned optimizer to a variety of neural network training tasks, where it outperforms the current state of the art learned optimizer -- at matched optimizer computational overhead -- with regard to optimization performance and meta-training speed, and is capable of generalization to tasks far different from those it was meta-trained on.
</details>

---


### [Tutorial on amortized optimization for learning to optimize over continuous domains](https://www.semanticscholar.org/paper/8198ec90c9e97f583f921451e7112d943da75cb4)
**Authors:** Amos, Brandon  
**Date:** 2022 · **Topics:** Surveys, Tutorials & Benchmarks  
*ArXiv* · 2022

*No abstract available.*

---


### [Learned Learning Rate Schedules for Deep Neural Network Training Using Reinforcement Learning](https://www.semanticscholar.org/paper/e8b22993efec83105daae948878a2c2ec0358c85)
**Authors:** Subramanian, Shreyas Vathul and Ganapathiraman, Vignesh and Gamal, Aly El  
**Date:** 2022 · **Topics:** Related Meta-Learning & Hyperparameter Adaptation  
*Tiny Papers @ ICLR* · 2022

*No abstract available.*

---


## 2021

### [Learning to Optimize: A Primer and A Benchmark.](https://www.semanticscholar.org/paper/f401a919db41eca28aa1cff062d98cc03b7ab66b)
**Authors:** Chen, Tianlong and Chen, Xiaohan and Chen, Wuyang and Heaton, Howard and Liu, Jialin and Wang, Zhangyang and Yin, Wotao  
**Date:** 2021-03-23 · **Topics:** Surveys, Tutorials & Benchmarks  
*arXiv: Optimization and Control* · 2021 · [arXiv:2103.12828](https://arxiv.org/abs/2103.12828)

<details>
<summary>Abstract</summary>

> Learning to optimize (L2O) is an emerging approach that leverages machine learning to develop optimization methods, aiming at reducing the laborious iterations of hand engineering. It automates the design of an optimization method based on its performance on a set of training problems. This data-driven procedure generates methods that can efficiently solve problems similar to those in the training. In sharp contrast, the typical and traditional designs of optimization methods are theory-driven, so they obtain performance guarantees over the classes of problems specified by the theory. The difference makes L2O suitable for repeatedly solving a certain type of optimization problems over a specific distribution of data, while it typically fails on out-of-distribution problems. The practicality of L2O depends on the type of target optimization, the chosen architecture of the method to learn, and the training procedure. This new paradigm has motivated a community of researchers to explore L2O and report their findings. This article is poised to be the first comprehensive survey and benchmark of L2O for continuous optimization. We set up taxonomies, categorize existing works and research directions, present insights, and identify open challenges. We also benchmarked many existing L2O approaches on a few but representative optimization problems. For reproducible research and fair benchmarking purposes, we released our software implementation and data in the package Open-L2O at https://github.com/VITA-Group/Open-L2O.
</details>

---


## 2020

### [Training Stronger Baselines for Learning to Optimize](https://www.semanticscholar.org/paper/3b5bd23386ded50640d285bc95d748272b23ca5c)
**Authors:** Chen, Tianlong and Zhang, Weiyi and Zhou, Jingyang and Chang, Shiyu and Liu, Sijia and Amini, Lisa and Yan, Shuicheng and Wang, Zhangyang  
**Date:** 2020-10-18 · **Topics:** General-Purpose Learned Optimizers  
*arXiv: Learning* · 2020 · [arXiv:2010.09089](https://arxiv.org/abs/2010.09089)

<details>
<summary>Abstract</summary>

> Learning to optimize (L2O) has gained increasing attention since classical optimizers require laborious problem-specific design and hyperparameter tuning. However, there is a gap between the practical demand and the achievable performance of existing L2O models. Specifically, those learned optimizers are applicable to only a limited class of problems, and often exhibit instability. With many efforts devoted to designing more sophisticated L2O models, we argue for another orthogonal, under-explored theme: the training techniques for those L2O models. We show that even the simplest L2O model could have been trained much better. We first present a progressive training scheme to gradually increase the optimizer unroll length, to mitigate a well-known L2O dilemma of truncation bias (shorter unrolling) versus gradient explosion (longer unrolling). We further leverage off-policy imitation learning to guide the L2O learning, by taking reference to the behavior of analytical optimizers. Our improved training techniques are plugged into a variety of state-of-the-art L2O models, and immediately boost their performance, without making any change to their model structures. Especially, by our proposed techniques, an earliest and simplest L2O model can be trained to outperform the latest complicated L2O models on a number of tasks. Our results demonstrate a greater potential of L2O yet to be unleashed, and urge to rethink the recent progress. Our codes are publicly available at: this https URL.
</details>

---


### [Tasks, stability, architecture, and compute: Training more effective learned optimizers, and using them to train themselves](https://www.semanticscholar.org/paper/8a858fb857abc06817d245bcb774a3901676f144)
**Authors:** Metz, Luke and Maheswaranathan, Niru and Freeman, Chris and Poole, Benjamin and Sohl-Dickstein, Jascha Narain  
**Date:** 2020-09-23 · **Topics:** General-Purpose Learned Optimizers  
*arXiv.org* · 2020 · [arXiv:2009.11243](https://arxiv.org/abs/2009.11243)

<details>
<summary>Abstract</summary>

> Much as replacing hand-designed features with learned functions has revolutionized how we solve perceptual tasks, we believe learned algorithms will transform how we train models. In this work we focus on general-purpose learned optimizers capable of training a wide variety of problems with no user-specified hyperparameters. We introduce a new, neural network parameterized, hierarchical optimizer with access to additional features such as validation loss to enable automatic regularization. Most learned optimizers have been trained on only a single task, or a small number of tasks. We train our optimizers on thousands of tasks, making use of orders of magnitude more compute, resulting in optimizers that generalize better to unseen tasks. The learned optimizers not only perform well, but learn behaviors that are distinct from existing first order optimizers. For instance, they generate update steps that have implicit regularization and adapt as the problem hyperparameters (e.g. batch size) or architecture (e.g. neural network width) change. Finally, these learned optimizers show evidence of being useful for out of distribution tasks such as training themselves from scratch.
</details>

---


## 2018

### [Understanding and correcting pathologies in the training of learned optimizers](https://www.semanticscholar.org/paper/cb4147fbd0704398c692667078efff935a36bb6d)
**Authors:** Metz, Luke and Maheswaranathan, Niru and Nixon, Jeremy and Freeman, Chris and Sohl-Dickstein, Jascha Narain  
**Date:** 2018-10-24 · **Topics:** General-Purpose Learned Optimizers  
*International Conference on Machine Learning* · 2018 · [arXiv:1810.10180](https://arxiv.org/abs/1810.10180)

<details>
<summary>Abstract</summary>

> Deep learning has shown that learned functions can dramatically outperform hand-designed functions on perceptual tasks. Analogously, this suggests that learned optimizers may similarly outperform current hand-designed optimizers, especially for specific problems. However, learned optimizers are notoriously difficult to train and have yet to demonstrate wall-clock speedups over hand-designed optimizers, and thus are rarely used in practice. Typically, learned optimizers are trained by truncated backpropagation through an unrolled optimization process resulting in gradients that are either strongly biased (for short truncations) or have exploding norm (for long truncations). In this work we propose a training scheme which overcomes both of these difficulties, by dynamically weighting two unbiased gradient estimators for a variational loss on optimizer performance, allowing us to train neural networks to perform optimization of a specific task faster than tuned first-order methods. We demonstrate these results on problems where our learned optimizer trains convolutional networks faster in wall-clock time compared to tuned first-order methods and with an improvement in test loss.
</details>

---


## 2017

### [Neural Optimizer Search with Reinforcement Learning](https://www.semanticscholar.org/paper/168b7d0ab57a331a228ce21ffd1becbb93066f79)
**Authors:** Bello, Irwan and Zoph, Barret and Vasudevan, Vijay and Le, Quoc V.  
**Date:** 2017-09-21 · **Topics:** Foundations of Learning to Optimize  
*arXiv: Artificial Intelligence* · 2017 · [arXiv:1709.07417](https://arxiv.org/abs/1709.07417)

<details>
<summary>Abstract</summary>

> We present an approach to automate the process of discovering optimization methods, with a focus on deep learning architectures. We train a Recurrent Neural Network controller to generate a string in a domain specific language that describes a mathematical update equation based on a list of primitive functions, such as the gradient, running average of the gradient, etc. The controller is trained with Reinforcement Learning to maximize the performance of a model after a few epochs. On CIFAR-10, our method discovers several update rules that are better than many commonly used optimizers, such as Adam, RMSProp, or SGD with and without Momentum on a ConvNet model. We introduce two new optimizers, named PowerSign and AddSign, which we show transfer well and improve training on a variety of different tasks and architectures, including ImageNet classification and Google's neural machine translation system.
</details>

---


### [Optimization as a Model for Few-Shot Learning](https://www.semanticscholar.org/paper/29c887794eed2ca9462638ff853e6fe1ab91d5d8)
**Authors:** Ravi, Sachin and Larochelle, Hugo  
**Date:** 2017-04-24 · **Topics:** Related Meta-Learning & Hyperparameter Adaptation  
*International Conference on Learning Representations* · 2017

*No abstract available.*

---


### [Learned optimizers that scale and generalize](https://www.semanticscholar.org/paper/b8ff7e02ffa1577d125acd3e998e8ce76a9059dc)
**Authors:** Wichrowska, Olga and Maheswaranathan, Niru and Hoffman, Matthew W. and Colmenarejo, Sergio Gómez and Denil, Misha and Freitas, Nando de and Sohl‐Dickstein, Jascha  
**Date:** 2017-03-14 · **Topics:** Foundations of Learning to Optimize  
*International Conference on Machine Learning* · 2017 · [arXiv:1703.04813](https://arxiv.org/abs/1703.04813)

<details>
<summary>Abstract</summary>

> Learning to learn has emerged as an important direction for achieving artificial intelligence. Two of the primary barriers to its adoption are an inability to scale to larger problems and a limited ability to generalize to new tasks. We introduce a learned gradient descent optimizer that generalizes well to new tasks, and which has significantly reduced memory and computation overhead. We achieve this by introducing a novel hierarchical RNN architecture, with minimal per-parameter overhead, augmented with additional architectural features that mirror the known structure of optimization tasks. We also develop a meta-training ensemble of small, diverse, optimization tasks capturing common properties of loss landscapes. The optimizer learns to outperform RMSProp/ADAM on problems in this corpus. More importantly, it performs comparably or better when applied to small convolutional neural networks, despite seeing no neural networks in its meta-training set. Finally, it generalizes to train Inception V3 and ResNet V2 architectures on the ImageNet dataset for thousands of steps, optimization problems that are of a vastly different scale than those it was trained on.
</details>

---


### [Learning Gradient Descent: Better Generalization and Longer Horizons](https://www.semanticscholar.org/paper/822e7515152e74626265c26b7aaccd2c654b5eba)
**Authors:** Lv, Kaifeng and Jiang, Shunhua and Li, Jian  
**Date:** 2017-03-10 · **Topics:** Foundations of Learning to Optimize  
*international conference on machine learning* · 2017 · [arXiv:1703.03633](https://arxiv.org/abs/1703.03633)

<details>
<summary>Abstract</summary>

> Training deep neural networks is a highly nontrivial task, involving carefully selecting appropriate training algorithms, scheduling step sizes and tuning other hyperparameters. Trying different combinations can be quite labor-intensive and time consuming. Recently, researchers have tried to use deep learning algorithms to exploit the landscape of the loss function of the training problem of interest, and learn how to optimize over it in an automatic way. In this paper, we propose a new learning-to-learn model and some useful and practical tricks. Our optimizer outperforms generic, hand-crafted optimization algorithms and state-of-the-art learning-to-learn optimizers by DeepMind in many tasks. We demonstrate the effectiveness of our algorithms on a number of tasks, including deep MLPs, CNNs, and simple LSTMs.
</details>

---


### [Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks](https://www.semanticscholar.org/paper/c889d6f98e6d79b89c3a6adf8a921f88fa6ba518)
**Authors:** Finn, Chelsea and Abbeel, Pieter and Levine, Sergey  
**Date:** 2017-03-09 · **Topics:** Related Meta-Learning & Hyperparameter Adaptation  
*International Conference on Machine Learning* · 2017 · [arXiv:1703.03400](https://arxiv.org/abs/1703.03400)

<details>
<summary>Abstract</summary>

> We propose an algorithm for meta-learning that is model-agnostic, in the sense that it is compatible with any model trained with gradient descent and applicable to a variety of different learning problems, including classification, regression, and reinforcement learning. The goal of meta-learning is to train a model on a variety of learning tasks, such that it can solve new learning tasks using only a small number of training samples. In our approach, the parameters of the model are explicitly trained such that a small number of gradient steps with a small amount of training data from a new task will produce good generalization performance on that task. In effect, our method trains the model to be easy to fine-tune. We demonstrate that this approach leads to state-of-the-art performance on two few-shot image classification benchmarks, produces good results on few-shot regression, and accelerates fine-tuning for policy gradient reinforcement learning with neural network policies.
</details>

---


### [Learning to Optimize Neural Nets](https://www.semanticscholar.org/paper/5b8e5804c3adeb4a4e60f8f7d8d76aab0e02cfbe)
**Authors:** Li, Ke and Malik, Jitendra  
**Date:** 2017-03-01 · **Topics:** Foundations of Learning to Optimize  
*arXiv: Learning* · 2017 · [arXiv:1703.00441](https://arxiv.org/abs/1703.00441)

<details>
<summary>Abstract</summary>

> Learning to Optimize is a recently proposed framework for learning optimization algorithms using reinforcement learning. In this paper, we explore learning an optimization algorithm for training shallow neural nets. Such high-dimensional stochastic optimization problems present interesting challenges for existing reinforcement learning algorithms. We develop an extension that is suited to learning optimization algorithms in this setting and demonstrate that the learned optimization algorithm consistently outperforms other known optimization algorithms even on unseen tasks and is robust to changes in stochasticity of gradients and the neural net architecture. More specifically, we show that an optimization algorithm trained with the proposed method on the problem of training a neural net on MNIST generalizes to the problems of training neural nets on the Toronto Faces Dataset, CIFAR-10 and CIFAR-100.
</details>

---


### [Learning to Learn without Gradient Descent by Gradient Descent](https://www.semanticscholar.org/paper/b5fdbacc37f1d5e1a72c292ac2107c06c7bd6d4f)
**Authors:** Chen, Yutian and Hoffman, Matthew W. and Colmenarejo, Sergio Gómez and Denil, Misha and Lillicrap, Timothy and Botvinick, Matt and Freitas, Nando de  
**Date:** 2016-11-11 · **Topics:** Foundations of Learning to Optimize  
*International Conference on Machine Learning* · 2017

*No abstract available.*

---


## 2016

### [Learning to reinforcement learn](https://www.semanticscholar.org/paper/282a380fb5ac26d99667224cef8c630f6882704f)
**Authors:** Wang, Jane X. and Kurth‐Nelson, Zeb and Tirumala, Dhruva and Soyer, Hubert and Leibo, Joel Z. and Munos, Rémi and Blundell, Charles and Kumaran, Dharshan and Botvinick, Matt  
**Date:** 2016-11-17 · **Topics:** Related Meta-Learning & Hyperparameter Adaptation  
*arXiv: Learning* · 2016 · [arXiv:1611.05763](https://arxiv.org/abs/1611.05763)

<details>
<summary>Abstract</summary>

> In recent years deep reinforcement learning (RL) systems have attained superhuman performance in a number of challenging task domains. However, a major limitation of such applications is their demand for massive amounts of training data. A critical present objective is thus to develop deep RL methods that can adapt rapidly to new tasks. In the present work we introduce a novel approach to this challenge, which we refer to as deep meta-reinforcement learning. Previous work has shown that recurrent networks can support meta-learning in a fully supervised context. We extend this approach to the RL setting. What emerges is a system that is trained using one RL algorithm, but whose recurrent dynamics implement a second, quite separate RL procedure. This second, learned RL algorithm can differ from the original one in arbitrary ways. Importantly, because it is learned, it is configured to exploit structure in the training domain. We unpack these points in a series of seven proof-of-concept experiments, each of which examines a key aspect of deep meta-RL. We consider prospects for extending and scaling up the approach, and also point out some potentially important implications for neuroscience.
</details>

---


### [Learning to learn by gradient descent by gradient descent](https://www.semanticscholar.org/paper/71683e224ab91617950956b5005ed0439a733a71)
**Authors:** Andrychowicz, Marcin and Denil, Misha and Gómez, Sergio Luis Suárez and Hoffman, Matthew W. and Pfau, David and Schaul, Tom and Shillingford, Brendan and Freitas, Nando de  
**Date:** 2016-06-14 · **Topics:** Foundations of Learning to Optimize  
*Neural Information Processing Systems* · 2016 · [arXiv:1606.04474](https://arxiv.org/abs/1606.04474)

<details>
<summary>Abstract</summary>

> The move from hand-designed features to learned features in machine learning has been wildly successful. In spite of this, optimization algorithms are still designed by hand. In this paper we show how the design of an optimization algorithm can be cast as a learning problem, allowing the algorithm to learn to exploit structure in the problems of interest in an automatic way. Our learned algorithms, implemented by LSTMs, outperform generic, hand-designed competitors on the tasks for which they are trained, and also generalize well to new tasks with similar structure. We demonstrate this on a number of tasks, including simple convex problems, training neural networks, and styling images with neural art.
</details>

---


### [Learning to Optimize](https://www.semanticscholar.org/paper/43c00597f8d59659af97dc35b24a836e8bd9b82a)
**Authors:** Li, Ke and Malik, Jitendra  
**Date:** 2016-06-06 · **Topics:** Foundations of Learning to Optimize  
*ICLR* · 2016

*No abstract available.*

---


## 2001

### [Learning to Learn Using Gradient Descent](https://www.semanticscholar.org/paper/044b2c29e0a54dc689786bd4d029b9ba6e355d58)
**Authors:** Hochreiter, Sepp and Younger, A. Steven and Conwell, Peter R.  
**Date:** 2001-08-17 · **Topics:** Foundations of Learning to Optimize  
*International Conference on Artificial Neural Networks* · 2001

*No abstract available.*

---

