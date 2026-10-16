# Awesome Layout Generation

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/wd1511/Awesome-Layout-Generation)

A curated bibliography of graphic layout generation, content-aware poster design, document layouts and editable graphic design.

**Last updated: 2026-10-16.** New entries are checked against arXiv records and official proceedings or author project pages. Unconfirmed publication venues remain labeled as arXiv; affiliations and additional resource links are included when verified. This is a curated collection, not an exhaustive index.

- [Dataset](#dataset)
- [2026](#2026)
- [2025](#2025)
- [2024](#2024)
- [2023](#2023)
- [2022](#2022)
- [2021](#2021)
- [2019-2020](#2019-2020)
- [Before](#before)
- [Reference](#reference)

Content-Agnostic and Content-Aware describe task conditioning; LLM-based describes a model family and may co-occur with either. Additional tags identify full-design generation, editing, surveys and evaluation.

## Dataset

### Content-agnostic Layout Generation

- Rico Dataset (ACM UIST 2017) [[Paper](http://ranjithakumar.net/resources/rico.pdf)] [[Download](http://www.interactionmining.org/rico.html#quick-downloads)] <br>
- PubLayNet Dataset (ICDAR 2019) [[Paper](http://arxiv.org/abs/1908.07836v1)] [[Download1](https://github.com/ibm-aur-nlp/PubLayNet)] [[Download2](https://drive.google.com/file/d/1eZMp9FiSUXixYedXhVKMQldJVvTehRMz/view)] <br>
- Magazine Dataset (SIGRAPH 2019) [[Paper](https://xtqiao.com/projects/content_aware_layout/paper.pdf)] [[Github](https://github.com/creative-graphic-design/huggingface-datasets_Magazine)] [[Download1](https://portland-my.sharepoint.com/personal/xqiao6-c_my_cityu_edu_hk/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fxqiao6%2Dc%5Fmy%5Fcityu%5Fedu%5Fhk%2FDocuments%2FWork%2FProject%2FDataset&ga=1)] [[Download2](https://huggingface.co/datasets/creative-graphic-design/Magazine)] <br>
- Crello Dataset (ICCV 2021) [[Paper](https://arxiv.org/abs/2108.01249)] [[Github](https://github.com/CyberAgentAILab/canvas-vae)] [[Download](https://github.com/CyberAgentAILab/canvas-vae/blob/main/docs/crello-dataset.md)] <br>
- DocLayNet Dataset (KDD 2022) [[Paper](https://arxiv.org/abs/2206.01062v1)] [[Download](https://github.com/DS4SD/DocLayNet)] [[Huggingface](https://huggingface.co/datasets/ds4sd/DocLayNet)] <br>
- WebUI Dataset (CHI 2023) [[Paper](https://arxiv.org/abs/2301.13280v1)] [[Download](https://uimodeling.github.io)] <br>
- M6Doc Dataset (CVPR 2023) [[Paper](https://arxiv.org/abs/2305.08719)] [[Download](https://github.com/HCIILAB/M6Doc)] <br>
- SciPostLayout (BMVC 2024) [[Paper](https://arxiv.org/abs/2407.19787)] [[Download](https://huggingface.co/datasets/omron-sinicx/scipostlayout_v2)] <br>

### Content-aware Layout Generation

- CGL Dataset v1 (IJCAI 2022) [[Paper](https://arxiv.org/abs/2205.00303)] [[Github](https://github.com/minzhouGithub/CGL-GAN)] [[Download](https://tianchi.aliyun.com/dataset/142692)] <br>
- CGL Dataset v2 (CIKM 2023) [[Paper](https://arxiv.org/abs/2306.09086)] [[Github](https://github.com/liuan0803/RADM?tab=readme-ov-file)] [[Download](https://github.com/liuan0803/RADM?tab=readme-ov-file)] <br>
- PKU PosterLayout Dataset (CVPR 2023) [[Paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Hsu_PosterLayout_A_New_Benchmark_and_Approach_for_Content-Aware_Visual-Textual_Presentation_CVPR_2023_paper.pdf)] [[Github](https://github.com/PKU-ICST-MIPL/PosterLayout-CVPR2023)] [[Download1(official)](http://39.108.48.32/mipl/PosterLayout/)] [[Download2(unofficial)](https://huggingface.co/datasets/creative-graphic-design/PKU-PosterLayout)] <br>

### Recent Layout and Graphic Design Datasets

- OmniDocLayout-1M (CVPR 2026) [[Paper](https://arxiv.org/abs/2510.26213)] [[Github](https://github.com/opendatalab/OmniDocLayout)] [[Download](https://huggingface.co/datasets/khr0516/OmniDocLayout-1M)] <br>
- Sketch-to-Layout datasets (ICCV 2025 Workshops) [[Paper](https://arxiv.org/abs/2510.27632)] [[Github / Data](https://github.com/google-deepmind/sketch_to_layout)] <br>
- GenPoster-100K (SEGA, ICCV 2025) [[Paper](https://arxiv.org/abs/2510.15749)] [[Project](https://brucew91.github.io/SEGA.github.io/)] [[Dataset](https://github.com/BruceW91/SEGA/tree/main/GenPoster-100K_Dataset)] <br>
- Layout-HF100k (Uni-Layout, ACMMM 2025) [[Paper](https://arxiv.org/abs/2508.02374)] [[Github / Data](https://github.com/JD-GenX/Uni-Layout)] <br>
- LICA: Layered Image Composition Annotations (2026) [[Paper](https://arxiv.org/abs/2603.16098)] [[Github](https://github.com/purvanshi-lica/lica-dataset)] [[Download](https://huggingface.co/datasets/lica-world/lica-dataset)] <br>

### Design Evaluation and Scientific Poster Benchmarks

- DesignSense (2026) [[Paper](https://arxiv.org/abs/2602.23438)] <br>
- TASTE (2026) [[Paper](https://arxiv.org/abs/2605.20731)] <br>
- Graphic-Design-Bench (NeurIPS 2026, accepted) [[Paper](https://arxiv.org/abs/2604.04192)] [[Github](https://github.com/purvanshi/lica-bench)] <br>
- PosterIQ (CVPR 2026) [[Paper](https://arxiv.org/abs/2603.24078)] [[Github](https://github.com/ArtmeScienceLab/PosterIQ-Benchmark)] <br>
- E-comIQ-ZH (CVPR 2026) [[Paper](https://arxiv.org/abs/2602.21698)] [[Github](https://github.com/4mm7/E-comIQ-ZH)] <br>
- Paper2Poster benchmark (NeurIPS 2025) [[Paper](https://arxiv.org/abs/2505.21497)] [[Project](https://paper2poster.github.io/)] [[Github / Data](https://github.com/Paper2Poster/Paper2Poster)] <br>
- P2P benchmark (ICLR 2026) [[Paper](https://arxiv.org/abs/2505.17104)] [[Github](https://github.com/multimodal-art-projection/P2P)] <br>

### Slide, Infographic and Structured Editing Benchmarks

- InstructEdit (content-edited layout generation, 2026) [[Paper](https://arxiv.org/abs/2610.17905)] <br>
- VisSlideBench (slide generation and editing, 2026) [[Paper](https://arxiv.org/abs/2610.16784)] [[Github / Data](https://github.com/VectorSpaceLab/InfoVis)] <br>
- InfoEdit (infographic editing and reflow, 2026) [[Paper](https://arxiv.org/abs/2609.33286)] [[Project](https://infoedit.github.io)] <br>
- VeriEdit-Bench (structured-asset editing, 2026) [[Paper](https://arxiv.org/abs/2610.04381)] [[Github / Data](https://github.com/flare200020/VeriEdit-Bench)] <br>
- CoDeLayout (ECCV 2026) [[Paper](https://arxiv.org/abs/2608.26716)] [[Project](https://hukcc.github.io/Beyond-Atomic-Layouts/)] <br>
- DeckQuiz (ReDeck, 2026) [[Paper](https://arxiv.org/abs/2609.00194)] [[Github / Data](https://github.com/microsoft/ReDeck)] <br>
- PPTBench (editable scientific-diagram reconstruction, 2026) [[Paper](https://arxiv.org/abs/2609.29718)] [[Project](https://lab.einsia.ai/pptbench)] <br>
- PresentBench (2026) [[Paper](https://arxiv.org/abs/2603.07244)] [[Project](https://presentbench.github.io)] <br>
- DECKBench (2026) [[Paper](https://arxiv.org/abs/2602.13318)] [[Github / Data](https://github.com/morgan-heisler/DeckBench)] <br>
- SlidesGen-Bench / Slides-Align1.5k (EMNLP 2026, accepted) [[Paper](https://arxiv.org/abs/2601.09487)] [[Github / Data](https://github.com/YunqiaoYang/SlidesGen-Bench)] <br>
- IGenBench (text-to-infographic reliability, 2026) [[Paper](https://arxiv.org/abs/2601.04498)] [[Project](https://igen-bench.vercel.app/)] <br>
- SlidesBench (AutoPresent, CVPR 2025) [[Paper](https://arxiv.org/abs/2501.00912)] [[Github / Data](https://github.com/para-lost/AutoPresent)] <br>

## 2026

**PLAYGROUND: Progressive Layout Generation with Render-Grounded Planning** <br>
*Jaeho Lee, Junhwan Heo, Junghyun Park, WonJun Moon, Eunju Yang, Seungho Jang, Seongchan Kim, Seungryong Kim.* <br>
arXiv 2026, KAIST AI <br>
**Content-Aware** **LLM-based** [[Paper](https://arxiv.org/abs/2610.18865)]
[[Project](https://cvlab-kaist.github.io/PlayGround/)] <br>

**AesCode: Aesthetic Code Generation with Decoupled Cross-Modal Rewards** <br>
*Xin Gao, Yifan Yang, Xin Li, Pan Wang, Yan Li, Muzhao Tian, Mingxi Cheng, Bei Liu, Kai Qiu, Qi Dai, Dong Chen, Yue Dong, Leandros Tassiulas, Rex Ying, Ji Li, Chong Luo.* <br>
arXiv 2026, Microsoft & Yale University & Nanyang Technological University & University of Pittsburgh & Shanghai Jiao Tong University & Fudan University <br>
**Graphic Design Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2610.18860)]
[[Project](https://microsoft.github.io/AesCode/)] <br>

**LayerCanvas: Infographic Generation in AI Learning Assistants via Hybrid Layer-Set Diffusion** <br>
*Keshav Gupta, Jeremy Owen, Christopher Lloyd, Shaunak Mishra, Manav Sharma.* <br>
arXiv 2026, University of California, San Diego & LinkedIn <br>
**Graphic Design Generation** [[Paper](https://arxiv.org/abs/2610.18763)] <br>

**Content-Edited Layout Generation for Graphic Design** <br>
*Shirong Yang, Zheyi Pan, Ying Cao.* <br>
arXiv 2026, ShanghaiTech University <br>
**Content-Aware** **Graphic Design Editing** [[Paper](https://arxiv.org/abs/2610.17905)] <br>

**InfoVis: Unified Slide Image Generation and Editing** <br>
*Jiahao Wang, Xiyan Jiang, Chenyuan Wu, Haoqiang Zhang, Xin Luo, Yueze Wang, Defu Lian, Bo Zhang, Jiajun Zhang, Zheng Liu.* <br>
arXiv 2026, Institute of Automation, Chinese Academy of Sciences & Beijing Academy of Artificial Intelligence & Zhejiang University & University of Science and Technology of China <br>
**Scientific Poster / Slide Generation** **Graphic Design Editing** [[Paper](https://arxiv.org/abs/2610.16784)]
[[Github](https://github.com/VectorSpaceLab/InfoVis)] <br>

**Stride: Scale-Aware Multi-Agent Evolutionary Refinement for Infographic Generation** <br>
*Yan Zhou, Yang Yang.* <br>
arXiv 2026, Shanghai Jiao Tong University <br>
**Graphic Design Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2610.13502)]
[[Github](https://github.com/SJTUSAI/Stride)] <br>

**From Prompting to Composing: A Spatial Canvas Interface for Poster Generation** <br>
*Yitong Wang, Fangyun Wei, Jinjing Zhao, Sirui Zhang, Hongyang Zhang, Dong Chen, Bo Dai, Yan Lu.* <br>
arXiv 2026, Fudan University & Microsoft Research & The University of Sydney & University of Science and Technology of China & University of Waterloo & The University of Hong Kong <br>
**Graphic Design Generation** [[Paper](https://arxiv.org/abs/2610.12230)]
[[Project](https://snowflakewang.github.io/Compo-Page/)]
[[Github](https://github.com/snowflakewang/Compo)] <br>

**CANDO: Cooperative Agentic Network for Layout Design Optimization** <br>
*Athanasios Masouris, Zheng Jing, Benjamin Sam Chandler, Hadi Jamali-Rad.* <br>
NeurIPS 2026 (accepted), Shell & Delft University of Technology <br>
**Content-Agnostic** **Content-Aware** **LLM-based** [[Paper](https://arxiv.org/abs/2610.10044)]
[[Conference](https://neurips.cc/virtual/2026/poster/153174)] <br>

**One Figure, Every Canvas: Editable Flowchart Relayout via Agentic Pipeline** <br>
*Shih-Chen Tseng, Chih-Hsuan Chen, Ryan Yang, Hsi-An Chen, Chun-Wei Tuan Mu, Yu-Lun Liu.* <br>
arXiv 2026, National Yang Ming Chiao Tung University & University of Illinois Urbana-Champaign <br>
**Graphic Design Editing** **LLM-based** [[Paper](https://arxiv.org/abs/2610.06852)]
[[Project](https://onefigureeverycanvas.vercel.app/)] <br>

**Beyond Plausibility: Verifiable Fine-Grained Image Editing on Structured Assets** <br>
*Muyao Wang, Chen Zhu, Shiqi Yang, DongHyun Hwan, Hideki Nakayama.* <br>
arXiv 2026, SB Intuitions & The University of Tokyo <br>
**Dataset / Evaluation** [[Paper](https://arxiv.org/abs/2610.04381)]
[[Github](https://github.com/flare200020/VeriEdit-Bench)] <br>

**InfoAgent: Traceable Generation and Repair of Evidence-Grounded Infographics** <br>
*Yifan Li, Tong Li, Qi Zeng, Lishuai Gao, Ruwei Pan, Cong Wei, Shaohua Kevin Zhou, Zhuoliang Kang, Xiaoming Wei.* <br>
arXiv 2026, University of Science and Technology of China & Meituan & Peking University <br>
**Graphic Design Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2609.39380)] <br>

**Back2Struct: Making Structured Images Editable Again** <br>
*Pengyu Yan, Yixin Wu, Yunjie Tian, David Doermann.* <br>
arXiv 2026, University at Buffalo, SUNY <br>
**Graphic Design Editing** **LLM-based** [[Paper](https://arxiv.org/abs/2609.37016)]
[[Project](https://pengyu965.github.io/Back2Struct.github.io)] <br>

**InfoEdit: Probing Global Layout Reasoning in Infographic Editing** <br>
*Cheng Yang, Chufan Shi, Huijuan Wang, Bo Shui, Yaokang Wu, Muzi Tao, Yibo Yan, Xuezhe Ma, Taylor Berg-Kirkpatrick.* <br>
arXiv 2026, University of California San Diego & University of Southern California & University of Illinois Urbana-Champaign & Carnegie Mellon University <br>
**Dataset / Evaluation** [[Paper](https://arxiv.org/abs/2609.33286)]
[[Project](https://infoedit.github.io)] <br>

**Planning and Rendering in Concert: DeepFusion of Autoregressive Layouts and Diffusion for Visual Text Generation** <br>
*Guanqiao Chen, Jingru Tan, Dongxing Mao, Catherine Chen, Zijian Du, Libo Qin, Hu Jian Guo, Alex Jinpeng Wang.* <br>
arXiv 2026, University of Science and Technology of China & Central South University & Louisiana State University & Arizona State University & Sun Yat-sen University <br>
**Graphic Design Generation** [[Paper](https://arxiv.org/abs/2609.22916)] <br>

**SlideLab: Audience-Centered Scientific Slide Generation and Evaluation** <br>
*Vidushee Vats, Karun Sharma, Yuxia Wang.* <br>
arXiv 2026, INSAIT, Sofia University <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2609.30294)] <br>

**Detect Anything in Graphic Design: Element-Level Rewards for Autoregressive Detection** <br>
*Jiangning Zhu, Bowen Li, Shenyu Qiao, Yima Gu, Zhao Zhang, Yuhui Yuan, Shixia Liu.* <br>
NeurIPS 2026 (accepted) <br>
**Graphic Design Editing** **LLM-based** [[Paper](https://arxiv.org/abs/2609.07072)]
[[Conference](https://neurips.cc/virtual/2026/poster/150451)] <br>

**SLIDEFORGE: An LLM Agent for Controllable Editing of Slides as Structured Artifacts** <br>
*Haozhen Zheng, Fulin Wang, Tianhu Xiong, Yingjie Yu, Shengyi Qian, Hanchao Yu, Alex Schwing, Klara Nahrstedt, Mingyuan Wu.* <br>
EMNLP 2026 (accepted), University of Illinois Urbana-Champaign & Meta <br>
**Graphic Design Editing** **Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2609.03109)]
[[Github](https://github.com/UIUC-MONET/SLIDEFORGE)] <br>

**ConvDeck: Conversational Paper-to-Slide Generation via Stage-Specific User Feedback** <br>
*Tarik Can Ozden, Sachidanand VS, Furkan Horoz, Ozgur Kara, Dilek Hakkani-Tür, Junho Kim, James Matthew Rehg.* <br>
Findings of EMNLP 2026 (accepted), University of Illinois Urbana-Champaign <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2609.00226)]
[[Project](https://convdeck.github.io)] <br>

**ReDeck: Step-Level Render-Grounded Refinement for Document-to-Slide Generation** <br>
*Muzhao Tian, Zezi Zeng, Yifan Yang, Xin Gao, Yan Li, Zisu Huang, Xiaohua Wang, Changze Lv, Mingxi Cheng, Bei Liu, Kai Qiu, Qi Dai, Dong Chen, Yue Dong, Xiaoqing Zheng, Ji Li, Chong Luo.* <br>
arXiv 2026, Microsoft & Shanghai Jiao Tong University & Xi’an Jiaotong University & Fudan University <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2609.00194)]
[[Github](https://github.com/microsoft/ReDeck)] <br>

**PPTBench: Can Coding Agents Reconstruct the Visual World through Structured, Editable Slides** <br>
*Xiaoqiu Wang, Yizhe Chi, Wenyi Li, Deyao Hong, Zhihan Shan, Mingju Gao, Kaisen Yang, Youjie Zheng, Calvin Xiao, Qinhuai Na.* <br>
arXiv 2026, Navers Lab, Einsia.AI & Tsinghua University <br>
**Dataset / Evaluation** [[Paper](https://arxiv.org/abs/2609.29718)]
[[Project](https://lab.einsia.ai/pptbench)] <br>

**Beyond Atomic Layouts: Compositional Design Understanding with Vision-Language Models** <br>
*Yiyang Huang, Zhaowen Wang, Simon Jenni, Jing Shi, Yitian Zhang, Yizhou Wang, Yun Fu.* <br>
ECCV 2026, Northeastern University & Adobe Research <br>
**Dataset / Evaluation** [[Paper](https://arxiv.org/abs/2608.26716)]
[[Project](https://hukcc.github.io/Beyond-Atomic-Layouts/)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4079)] <br>

**ACE: A Self-Correcting Agentic Canvas Editor for Multi-Slide Presentation Automation** <br>
*JooYoung Jang, Taegyeong Lee, Jihyeon Park, Nojun Kwak.* <br>
EMNLP 2026 Industry Track (accepted), Seoul National University & Miridih <br>
**Graphic Design Editing** **Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2608.24103)]
[[Github](https://github.com/BloomBerry/agentic-canvas-editor)]
[[Dataset](https://huggingface.co/datasets/BloomBerry/figma-slide-benchmark)] <br>

**SeaSlides: Semantic Abstraction Layer for Agentic Slide Generation** <br>
*Shengjun Fang, Chenyang Wu, Zongzhang Zhang.* <br>
arXiv 2026 <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2608.03298)] <br>

**Personalization as Inverse Planning: Learning Latent Design Intents for Agentic Slide Generation via Structural Denoising** <br>
*Tianci Liu, Zihan Dong, Linjun Zhang, Haoyu Wang, Jing Gao, Emre Kiciman, Ranveer Chandra, Wei-Ting Chen.* <br>
ECCV 2026, Purdue University & Rutgers University & University at Albany & Microsoft <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2607.00407)] <br>

**X+Slides: Benchmarking Audience-Conditioned Slide Generation** <br>
*Haodong Chen, Xuanhe Zhou, Wei Zhou, Xinyue Shao, Yanbing Zhu, Bo Wang, Jiawei Hong, Anya Jia, Fan Wu.* <br>
arXiv 2026, Shanghai Jiao Tong University & Harbin Institute of Technology & SenseTime <br>
**Dataset / Evaluation** [[Paper](https://arxiv.org/abs/2606.19256)] <br>

**MemSlides: A Hierarchical Memory Driven Agent Framework for Personalized Slide Generation with Multi-turn Local Revision** <br>
*Ye Jin, Yangyang Xu, Jun Zhu, Yibo Yang.* <br>
arXiv 2026, Beijing University of Posts and Telecommunications & Tsinghua University & Shanghai Jiao Tong University <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2606.17162)]
[[Github](https://github.com/huohua325/Memslides)]
[[Project](https://memslides.com/)]
[[Project](https://memslides.github.io/)] <br>

**UniPPTBench: A Unified Benchmark for Presentation Generation Across Diverse Input Settings** <br>
*Bo Zhao, Maosheng Pang, Chen Zhang, Huan Yang, Yixin Cao, Wei Ji.* <br>
arXiv 2026 <br>
**Dataset / Evaluation** [[Paper](https://arxiv.org/abs/2605.17356)] <br>

**PresentAgent-2: Towards Generalist Multimodal Presentation Agents** <br>
*Wei Wu, Ziyang Xu, Zeyu Zhang, Yang Zhao, Hao Tang.* <br>
arXiv 2026, La Trobe University & Peking University <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2605.11363)]
[[Github](https://github.com/AIGeeksGroup/PresentAgent-2)]
[[Project](https://aigeeksgroup.github.io/PresentAgent-2)] <br>

**ECHO: Explainable Co-editing with Human-in-the-loop Operations for Presentation Refinement** <br>
*Yu Fu, Yongqi Kang, Yujia Zhou, Yong Zhao.* <br>
arXiv 2026, Sichuan University <br>
**Graphic Design Editing** **Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2606.09851)] <br>

**Narrative-Driven Paper-to-Slide Generation via ArcDeck** <br>
*Tarik Can Ozden, Sachidanand VS, Furkan Horoz, Ozgur Kara, Junho Kim, James Matthew Rehg.* <br>
arXiv 2026, University of Illinois Urbana-Champaign & Middle East Technical University <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2604.11969)]
[[Github](https://github.com/RehgLab/ArcDeck)]
[[Project](https://arcdeck.org/)] <br>

**Show Me the Infographic I Imagine: Intent-Aware Infographic Retrieval for Authoring Support** <br>
*Jing Xu, Jiarui Hu, Zhihao Shuai, Yiyun Chen, Weikai Yang.* <br>
arXiv 2026, The Hong Kong University of Science and Technology (Guangzhou) & Nanjing University <br>
**Graphic Design Editing** **LLM-based** [[Paper](https://arxiv.org/abs/2604.07989)]
[[Project](https://infographicretrieval.github.io/)] <br>

**Design First, Code Later: Aesthetically Pleasing Template-Free Slides Generation** <br>
*Zhiyao Cui, Chenxu Wang, Shuyue Hu, Yiqun Zhang, Wenqi Shao, Qiaosheng Zhang, Zhen Wang.* <br>
arXiv 2026, Northwestern Polytechnical University & Shanghai Artificial Intelligence Laboratory & Shanghai Innovation Institution & Fudan University <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2605.26451)]
[[Github](https://github.com/sxswz213/DeepSlides)] <br>

**Learning to Present: Inverse Specification Rewards for Agentic Slide Generation** <br>
*Karthik Ragunath Ananda Kumar, Subrahmanyam Arunachalam.* <br>
arXiv 2026, Tavus & The University of Texas at Dallas & Texas A&M University <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2603.16839)]
[[Dataset](https://huggingface.co/datasets/KarthikRagunathAnandaKumar/sliderl-multi-turn-rollouts)]
[[Github](https://github.com/pushing-the-frontier/slide-forge-llm)] <br>

**PresentBench: A Fine-Grained Rubric-Based Benchmark for Slide Generation** <br>
*Xin-Sheng Chen, Jiayu Zhu, Pei-lin Li, Hanzheng Wang, Shuojin Yang, Meng-Hao Guo.* <br>
arXiv 2026, Tsinghua University <br>
**Dataset / Evaluation** [[Paper](https://arxiv.org/abs/2603.07244)]
[[Project](https://presentbench.github.io)] <br>

**InfoAlign: A Human-AI Co-Creation System for Storytelling with Infographics** <br>
*Jielin Feng, Xinwu Ye, Qianhui Li, Verena Ingrid Prantl, Jun-Hsiang Yao, Yuheng Zhao, Yun Wang, Siming Chen.* <br>
CHI 2026, Fudan University & The University of Hong Kong & University of Vienna & Microsoft Research Asia <br>
**Graphic Design Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2602.22901)]
[[Proceedings](https://doi.org/10.1145/3772318.3791844)] <br>

**DeepPresenter: Environment-Grounded Reflection for Agentic Presentation Generation** <br>
*Hao Zheng, Guozhao Mo, Xinru Yan, Qianhao Yuan, Wenkai Zhang, Xuanang Chen, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun.* <br>
arXiv 2026, Institute of Software, Chinese Academy of Sciences & University of Chinese Academy of Sciences <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2602.22839)]
[[Github](https://github.com/icip-cas/PPTAgent)] <br>

**EvoDesign: Agentic Editable Diagram Creation via Design Expertise Evolution** <br>
*Tianfu Wang, Leilei Ding, Ziyang Tao, Yi Zhan, Zhiyuan Ma, Wei Wu, Yuxuan Lei, Junyang Wang, Yin Wu, Yizhao Xu, Hongyuan Zhu, Qi Liu, Nicholas Jing Yuan, Yanyong Zhang, Hui Xiong.* <br>
NeurIPS 2026 (accepted) <br>
**Graphic Design Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2604.09568)]
[[Github](https://github.com/AuraX-AI/EvoDiagram)]
[[Conference](https://neurips.cc/virtual/2026/poster/154437)] <br>

**DECKBench: Benchmarking Multi-Agent Frameworks for Academic Slide Generation and Editing** <br>
*Daesik Jang, Morgan Lindsay Heisler, Linzi Xing, Yifei Li, Edward Wang, Ying Xiong, Yong Zhang, Zhenan Fan.* <br>
arXiv 2026, Huawei Technologies Canada & The University of British Columbia <br>
**Dataset / Evaluation** [[Paper](https://arxiv.org/abs/2602.13318)]
[[Github](https://github.com/morgan-heisler/DeckBench)] <br>

**From Dead Pixels to Editable Slides: Infographic Reconstruction into Native Google Slides via Vision-Language Region Understanding** <br>
*Leonardo Gonzalez.* <br>
WWW 2026 Companion, Trilogy AI Center of Excellence <br>
**Graphic Design Editing** **Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2602.07645)] <br>

**PaperX: A Unified Framework for Multimodal Academic Presentation Generation with Scholar DAG** <br>
*Tao Yu, Minghui Zhang, Zhiqing Cui, Hao Wang, Zhongtian Luo, Shenghua Chai, Junhao Gong, Yuzhao Peng, Yuxuan Zhou, Yujia Yang, Zhenghao Zhang, Haopeng Jin, Xinming Wang, Yufei Xiong, Jiabing Yang, Jiahao Yuan, Hanqing Wang, Hongzhu Yi, Yan Huang, Liang Wang.* <br>
arXiv 2026, Institute of Automation, Chinese Academy of Sciences & University of Chinese Academy of Sciences & Peking University & Tsinghua University & The Hong Kong University of Science and Technology (Guangzhou) <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2602.03866)]
[[Github](https://github.com/yutao1024/PaperX)] <br>

**SlidesGen-Bench: Evaluating Slides Generation via Computational and Quantitative Metrics** <br>
*Yunqiao Yang, Wenbo Li, Houxing Ren, Zimu Lu, Ke Wang, Zhiyuan Huang, Zhuofan Zong, Mingjie Zhan, Hongsheng Li.* <br>
EMNLP 2026 (accepted), The Chinese University of Hong Kong & SenseTime Research & CPII under InnoHK & Shanghai AI Laboratory <br>
**Dataset / Evaluation** [[Paper](https://arxiv.org/abs/2601.09487)]
[[Github](https://github.com/YunqiaoYang/SlidesGen-Bench)] <br>

**IGenBench: Benchmarking the Reliability of Text-to-Infographic Generation** <br>
*Yinghao Tang, Xueding Liu, Boyuan Zhang, Tingfeng Lan, Yupeng Xie, Jiale Lao, Yiyao Wang, Haoxuan Li, Tingting Gao, Bo Pan, Luoxuan Weng, Xiuqi Huang, Minfeng Zhu, Yingchaojie Feng, Yuyu Luo, Wei Chen.* <br>
arXiv 2026, Zhejiang University & University of Electronic Science and Technology of China & University of Virginia & The Hong Kong University of Science and Technology (Guangzhou) & Cornell University & National University of Singapore <br>
**Dataset / Evaluation** [[Paper](https://arxiv.org/abs/2601.04498)]
[[Project](https://igen-bench.vercel.app/)] <br>

**i-Design: Step-by-Step Graphic Layout Design with Progressive Aesthetic Policy Optimization** <br>
*Sohan Patnaik, Rishabh Jain, Balaji Krishnamurthy, Mausoom Sarkar.* <br>
ECCV 2026 <br>
**Content-Agnostic** **LLM-based** [[Paper](https://eccv.ecva.net/virtual/2026/poster/5750)] <br>

**PosterCopilot: Toward Layout Reasoning and Controllable Editing for Professional Graphic Design** <br>
*Jiazhe Wei, Ken Li, Tianyu Lao, Haofan Wang, Liang Wang, Caifeng Shan, Chenyang Si.* <br>
ECCV 2026, LibLib.ai & PRLab, Nanjing University & Institute of Automation, Chinese Academy of Sciences <br>
**Content-Aware** **LLM-based** [[Paper](https://arxiv.org/abs/2512.04082)]
[[Project](https://postercopilot.github.io/)]
[[Conference](https://eccv.ecva.net/virtual/2026/poster/4148)] <br>

**PosterDuet: Co-Evolving Design Generation and Reward Optimization for Product Poster Synthesis** <br>
*Junlong Wu, Pengcheng Wei, Jia Sun, Huaiqing Wang, Weixuan Zeng, Zijun Li, Honglie Wang, Yongrui Heng, Boheng Zhang, Dewen Fan, Fan Yang, Tingting Gao, Houde Liu, Qianqian Gan.* <br>
NeurIPS 2026 (accepted) <br>
**Graphic Design Generation** **Graphic Design Editing** **LLM-based** [[Paper](https://openreview.net/forum?id=8v51RaMEuy)]
[[Conference](https://neurips.cc/virtual/2026/poster/155036)] <br>

**VisEditBench: A Benchmark for Vector-Format Diagram Editing with Visual Instructions** <br>
*Akito Taneguchi, Itsumi Saito, Haruto Yoshida, Jun Suzuki.* <br>
NeurIPS 2026 (accepted) <br>
**Dataset / Evaluation** [[Paper](https://openreview.net/forum?id=e4d9v8gOoV)]
[[Conference](https://neurips.cc/virtual/2026/poster/139221)] <br>

**Designer-RSI: Evolving Procedural Memory from User Traffic for Agentic Graphic Design** <br>
*Hongyang Du, Lan Yan, Christian Flores, Asim Kadav.* <br>
arXiv 2026, Adobe & Brown University <br>
**Graphic Design Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2609.22086)] <br>

**Human-aware Design Generation: Adding 3D Humans into Graphic Designs** <br>
*Zijin Hou, Ying Cao.* <br>
ACMMM 2026, ShanghaiTech University, Shanghai, China <br>
**Graphic Design Generation** [[Paper](https://arxiv.org/abs/2609.17689)]
[[Github](https://github.com/GreyNails/Human-aware-Design-Generation-Adding-3D-Humans-into-Graphic-Designs)] <br>

**From Transient Prompts to Persistent Control: Scientific Poster Generation via Recursive Semantic-Geometric Contracts** <br>
*Runze Li, Yukun Zhao, Can Xu, Yucheng Shen, Shuaiqiang Wang, Jianmin Wu, Lingyong Yan, Dawei Yin.* <br>
arXiv 2026 <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2609.17326)] <br>

**Learning Interaction between Image and Layout Priors for Joint Image-Layout Generation in Design Templates** <br>
*Shirong Yang, Bo Yang, Ying Cao.* <br>
arXiv 2026, ShanghaiTech University <br>
**Content-Aware** [[Paper](https://arxiv.org/abs/2609.11519)] <br>

**GDB-Reward: From Evaluation Metrics to Training Rewards for Graphic Design** <br>
*Adrienne Deganutti, Purvanshi Mehta, Simon Hadfield, Andrew Gilbert.* <br>
arXiv 2026 <br>
**Dataset / Evaluation** [[Paper](https://arxiv.org/abs/2609.02813)] <br>

**Giraffe: A Mapping Architecture from Hidden Text Representations to Visual Embeddings for Efficient Graphic Design** <br>
*Nejla Ghaboosi.* <br>
arXiv 2026, Canva Research <br>
**Graphic Design Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2608.23970)] <br>

**TextRefine: Improving Textual Fidelity, Spatial Placement, and Glyph Rendering for Text Editing in Product Posters** <br>
*Honglie Wang, Jia Sun, Zijun Li, Junlong Wu, Pengcheng Wei, Jiyuan Wang, Yongrui Heng, Boheng Zhang, Huaiqing Wang, Dewen Fan, Qianqian Gan, Fan Yang, Tingting Gao, Yan-Ming Zhang.* <br>
arXiv 2026 <br>
**Graphic Design Editing** [[Paper](https://arxiv.org/abs/2608.19637)] <br>

**Mise-en-Scène: Implicit Layout Emergence in Diffusion Transformers for Human-AI Design Co-Creation** <br>
*Zipeng Xu, Ryan Murdock, Umberto Michieli.* <br>
ECCV 2026 Workshops, Canva Research <br>
**Graphic Design Generation** [[Paper](https://arxiv.org/abs/2608.19000)] <br>

**PosterText: Towards Unified Visual Text Generation and Editing for E-commerce Poster** <br>
*Xiaoan Liu, Lichen Ma, Zipeng Guo, Yu He, Xiaoyan Su, Shaojie Guo, Jingling Fu, Xiaolong Fu, Hao Yang, Tongxuan Liu, Yu Guo, Fei Wang, Xinyi Liu, Yongjun Zhang, Junshi Huang.* <br>
arXiv 2026 <br>
**Graphic Design Generation** [[Paper](https://arxiv.org/abs/2608.16289)] <br>

**PosterMELD: Multi-Agent Paper-to-Poster Generation for Controllable Design Diversity with Editable Print-Ready Outputs** <br>
*Haojie Hu, Chenhao Dang, Yaojia Liu, Hengrui Kang, Conghui He, Weijia Li.* <br>
arXiv 2026 <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2608.02218)]
[[Github](https://github.com/Shannon4Science/PosterMELD)] <br>

**SG-Layout: Structured Scene Graph-Guided Layout Generation with LLMs** <br>
*Junsheng Wang, Chao Chen, Mengying Xie, Mingyan Li, Fuqiang Gu.* <br>
WAICA 2026, Chongqing University, Chongqing, China <br>
**Content-Agnostic** **LLM-based** [[Paper](https://arxiv.org/abs/2608.01106)] <br>

**StructuredEdit: Constraint-Aware Graphic Design Editing via Differentiable Parameter Propagation** <br>
*Veeramanohar Avudaiappan, Ritwik Murali.* <br>
arXiv 2026, Department of Electrical and Electronics Engineering, Amrita School of Engineering, Coimbatore, Amrita Vishwa Vidyapeetham, India & Department of Computer Science and Engineering, Amrita School of Computing, Coimbatore, Amrita Vishwa Vidyapeetham, India <br>
**Graphic Design Editing** [[Paper](https://arxiv.org/abs/2607.04612)] <br>

**ResearchStudio-Reel: Automate the Last Mile of Research from Paper to Poster, Video, and Blog** <br>
*Lingao Xiao, Yalun Dai, Yangyu Huang, Qihao Zhao, Wenshan Wu, Hugo He, Ruishuo Chen, Jin Jiang, Qianli Ma, Jiahuan Zhang, Xin Zhang, Ying Xin, Yang Ou, Yan Xia, Scarlett Li, Longbo Huang, Zhipeng Zhang, Yang He, Yap Kim Hui, Yan Lu.* <br>
arXiv 2026, Microsoft Research & National University of Singapore & Nanyang Technological University & Tsinghua University & Peking University & Shanghai Jiao Tong University & Westlake University & A*STAR <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2607.04438)]
[[Github](https://github.com/hugohe3/ppt-master)] <br>

**PosterHarness: Turning Scientific Poster Generation into an Auditable Instruction-Following Benchmark** <br>
*Tianyi Yang, Dawei Fu, Youpeng Wu, Zixun Kou, Linrui Chen, Ruobing Jiang, Zijian Wang, Qiang Li.* <br>
arXiv 2026, School of Physics, Peking University <br>
**Dataset / Evaluation** [[Paper](https://arxiv.org/abs/2607.03006)] <br>

**Aggregating LLM-Based Weak Verifiers for Spatial Layout Generation** <br>
*Sharon Zhang, R. Kenny Jones, Jiajun Wu, Maneesh Agrawala.* <br>
arXiv 2026, Stanford University, Stanford, California, USA & Roblox, San Mateo, California, USA <br>
**Dataset / Evaluation** [[Paper](https://arxiv.org/abs/2606.05268)] <br>

**Any2Poster: Any-Source Poster Generation Across Modalities and Domains** <br>
*Amogh Vinaykumar, Aiden Li, Suozhi Huang, Shilong Liu.* <br>
arXiv 2026, Flower Mound High School & University College London & Princeton University <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2606.02915)]
[[Github](https://github.com/Any2Poster/Any2Poster)]
[[Project](https://any2poster.github.io/Any2Poster/)] <br>

**TASTE: A Designer-Annotated Multi-Dimensional Preference Dataset for AI-Generated Graphic Design** <br>
*Haonan Zhu, Elad Hirsch, Alexandria Minetti, Allison Nulty, Ben Huffman, Purvanshi Mehta.* <br>
arXiv 2026, Lica World, San Francisco, USA & Contra.Work Inc., Brooklyn, NY, USA <br>
**Dataset / Evaluation** [[Paper](https://arxiv.org/abs/2605.20731)] <br>

**SIMPLEPOSTER: A SIMPLE BASELINE FOR PRODUCT POSTER GENERATION** <br>
*Benlei Cui, Fangao Zeng, Weitao Jiang, Yuwen Zhai, Haiwen Hong, Longtao Huang, Hui Xue, Wenxiang Shang, Pipei Huang.* <br>
CVPR 2026, Taobao & Tmall Group, Alibaba Group & Yuvion Team, Alibaba Group <br>
**Graphic Design Generation** [[Paper](https://arxiv.org/abs/2605.08784)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Cui_SIMPLEPOSTER_A_SIMPLE_BASELINE_FOR_PRODUCT_POSTER_GENERATION_CVPR_2026_paper.html)]
[[Github](https://github.com/Alibaba-YuFeng/SIMPLEPOSTER)]
[[Github](https://github.com/Alibaba-VELLDEPTH/SIMPLEPOSTER)] <br>

**CreatiParser: Generative Image Parsing of Raster Graphic Designs into Editable Layers** <br>
*Weidong Chen, Dexiang Hong, Zhendong Mao, Yutao Cheng, Xinyan Liu, Lei Zhang, Yongdong Zhang.* <br>
arXiv 2026 <br>
**Graphic Design Editing** [[Paper](https://arxiv.org/abs/2604.19632)] <br>

**AeSlides: Incentivizing Aesthetic Layout in LLM-Based Slide Generation via Verifiable Rewards** <br>
*Yiming Pan, Chengwei Hu, Xuancheng Huang, Can Huang, Mingming Zhao, Yuean Bi, Xiaohan Zhang, Aohan Zeng, Linmei Hu.* <br>
arXiv 2026, Beijing Institute of Technology & Zhipu AI (Z.ai) <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2604.22840)]
[[Github](https://github.com/ympan0508/aeslides)] <br>

**Brief2Design: A Multi-phased, Compositional Approach to Prompt-based Graphic Design** <br>
*Kotaro Kikuchi, Nami Ogawa.* <br>
arXiv 2026, CyberAgent, Tokyo, Japan <br>
**Graphic Design Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2604.11019)] <br>

**ReContraster: Making Your Posters Stand Out with Regional Contrast** <br>
*Peixuan Zhang, Zijian Jia, Ziqi Cai, Shuchen Weng, Si Li, Boxin Shi.* <br>
arXiv 2026, State Key Laboratory for Multimedia Information Processing, School of Computer Science, Peking University & National Engineering Research Center of Visual Technology, School of Computer Science, Peking University & Beijing Academy of Artificial Intelligence & School of Artificial Intelligence, Beijing University of Posts and Telecommunications <br>
**Graphic Design Editing** [[Paper](https://arxiv.org/abs/2604.10442)] <br>

**GAN-based Domain Adaptation for Image-aware Layout Generation in Advertising Poster Design** <br>
*Chenchen Xu, Min Zhou, Tiezheng Ge, Weiwei Xu.* <br>
arXiv 2026, Anhui Normal University & Zhejiang University & Shenzhen Bay Laboratory & Alibaba Group <br>
**Content-Aware** [[Paper](https://arxiv.org/abs/2604.07409)] <br>

**A Diagnostic Benchmark for Layered Layout and Template-Variant Reasoning** <br>
*Jaejung Seol, Haonan Zhu, Elad Hirsch, Adrienne Deganutti, Purvanshi Mehta.* <br>
NeurIPS 2026 (accepted), Lica World <br>
*Earlier preprint: Graphic-Design-Bench: A Comprehensive Benchmark for Evaluating AI on Graphic Design Tasks.* <br>
**Dataset / Evaluation** [[Paper](https://openreview.net/forum?id=GVMikNSGQx)]
[[Preprint](https://arxiv.org/abs/2604.04192)]
[[Conference](https://neurips.cc/virtual/2026/poster/139592)]
[[Github](https://github.com/purvanshi/lica-bench)] <br>

**iPoster: Content-Aware Layout Generation for Interactive Poster Design via Graph-Enhanced Diffusion Models** <br>
*Xudong Zhou, Jinyuan Liang, Qiuyi Guo, Guozheng Li.* <br>
CHI EA 2026, Beijing Institute of Technology, Beijing, China <br>
**Content-Aware** [[Paper](https://arxiv.org/abs/2603.29469)] <br>

**PosterIQ: A Design Perspective Benchmark for Poster Understanding and Generation** <br>
*Yuheng Feng, Wen Zhang, Haodong Duan, Xingxing Zou.* <br>
CVPR 2026, The Hong Kong Polytechnic University & Snapchat Inc & ByteDance Seed <br>
**Dataset / Evaluation** [[Paper](https://arxiv.org/abs/2603.24078)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Feng_PosterIQ_A_Design_Perspective_Benchmark_for_Poster_Understanding_and_Generation_CVPR_2026_paper.html)]
[[Github](https://github.com/ArtmeScienceLab/PosterIQ-Benchmark)] <br>

**Seeing is Improving: Visual Feedback for Iterative Text Layout Refinement** <br>
*Junrong Guo, Shancheng Fang, Yadong Qu, Hongtao Xie.* <br>
CVPR 2026, University of Science and Technology of China & Shenzhen University <br>
**Graphic Design Editing** [[Paper](https://arxiv.org/abs/2603.22187)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Guo_Seeing_is_Improving_Visual_Feedback_for_Iterative_Text_Layout_Refinement_CVPR_2026_paper.html)]
[[Github](https://github.com/FolSpark/VFLM)] <br>

**LICA: Layered Image Composition Annotations for Graphic Design Research** <br>
*Elad Hirsch, Shubham Yadav, Mohit Garg, Purvanshi Mehta.* <br>
arXiv 2026, Lica World <br>
**Dataset / Evaluation** [[Paper](https://arxiv.org/abs/2603.16098)]
[[Github](https://github.com/purvanshi-lica/lica-dataset)]
[[Dataset](https://huggingface.co/datasets/lica-world/lica-dataset)] <br>

**InnoAds-Composer: Efficient Condition Composition for E-Commerce Poster Generation** <br>
*Yuxin Qin, Ke Cao, Haowei Liu, Ao Ma, Fengheng Li, Honghe Zhu, Zheng Zhang, Run Ling, Wei Feng, Xuanhua He, Zhanjie Zhang, Zhen Guo, Haoyi Bian, Jingjing Lv, Junjie Shen, Ching Law.* <br>
CVPR 2026, JD.com, Inc., Beijing, China & The Hong Kong University of Science and Technology, Hong Kong, China & Chongqing University of Posts and Telecommunications, Chongqing, China & Zhejiang University, Hangzhou, China <br>
**Graphic Design Generation** [[Paper](https://arxiv.org/abs/2603.05898)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Qin_InnoAds-Composer_Efficient_Condition_Composition_for_E-Commerce_Poster_Generation_CVPR_2026_paper.html)] <br>

**DesignSense: A Human Preference Dataset and Reward Modeling Framework for Graphic Layout Generation** <br>
*Varun Gopal, Rishabh Jain, Aradhya Mathur, Nikitha SR, Sohan Patnaik, Sudhir Yarram, Mayur Hemani, Balaji Krishnamurthy, Mausoom Sarkar.* <br>
arXiv 2026, MDSR, Adobe <br>
**Dataset / Evaluation** [[Paper](https://arxiv.org/abs/2602.23438)] <br>

**EfficientPosterGen: Semantic-aware Efficient Poster Generation via Token Compression and Accurate Violation Detection** <br>
*Wenxin Tang, Jingyu Xiao, Yanpei Gong, Fengyuan Ran, Tongchuan Xia, Junliang Liu, Man Ho Lam, Wenxuan Wang, Michael R. Lyu.* <br>
arXiv 2026, Tsinghua University, Beijing, China & The Chinese University of Hong Kong, Hong Kong, China & Harbin Institute of Technology, Harbin, China & Wuhan University, Wuhan, China & Beijing University of Posts and Telecommunications, Beijing, China & Dalian Maritime University, Dalian, China & Renmin University of China, Beijing, China <br>
**Graphic Design Generation** [[Paper](https://arxiv.org/abs/2603.00155)]
[[Github](https://github.com/vinsontang1/EfficientPosterGen-Code)] <br>

**E-comIQ-ZH: A Human-Aligned Dataset and Benchmark for Fine-Grained Evaluation of E-commerce Posters with Chain-of-Thought** <br>
*Meiqi Sun, Mingyu Li, Junxiong Zhu.* <br>
CVPR 2026, Taobao & Tmall Group, Alibaba Group <br>
**Dataset / Evaluation** [[Paper](https://arxiv.org/abs/2602.21698)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_E-comIQ-ZH_A_Human-Aligned_Dataset_and_Benchmark_for_Fine-Grained_Evaluation_of_CVPR_2026_paper.html)]
[[Github](https://github.com/4mm7/E-comIQ-ZH)] <br>

**PosterReward: Unlocking Accurate Evaluation for High-Quality Graphic Design Generation** <br>
*Jianyu Lai, Sixiang Chen, Jialin Gao, Hengyu Shi, Zhongying Liu, Fuxiang Zhai, Junfeng Luo, Xiaoming Wei, Lujia Wang, Lei Zhu.* <br>
CVPR 2026, The Hong Kong University of Science and Technology (Guangzhou), & Meituan & The Hong Kong University of Science and Technology <br>
**Dataset / Evaluation** [[Paper](https://arxiv.org/abs/2603.29855)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Lai_PosterReward_Unlocking_Accurate_Evaluation_for_High-Quality_Graphic_Design_Generation_CVPR_2026_paper.html)]
[[Project](https://alexlai2860.github.io/PosterReward/)] <br>

**From Pixels to Policies: Reinforcing Spatial Reasoning in Language Models for Content-Aware Layout Design** <br>
*Sha Li, Stefano Petrangeli, Yu Shen, Xiang Chen.* <br>
ACL 2026 Industry Track, Virginia Tech & Adobe Research <br>
**Content-Aware** **LLM-based** [[Paper](https://arxiv.org/abs/2602.13912)]
[[Proceedings](https://aclanthology.org/2026.acl-industry.104/)] <br>

**PosterOmni: Generalized Artistic Poster Creation via Task Distillation and Unified Reward Feedback** <br>
*Sixiang Chen, Jianyu Lai, Jialin Gao, Hengyu Shi, Zhongying Liu, Tian Ye, Junfeng Luo, Xiaoming Wei, Lei Zhu.* <br>
CVPR 2026, The Hong Kong University of Science and Technology (Guangzhou), & Meituan, & The Hong Kong University of Science and Technology <br>
**Graphic Design Generation** [[Paper](https://arxiv.org/abs/2602.12127)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_PosterOmni_Generalized_Artistic_Poster_Creation_via_Task_Distillation_and_Unified_CVPR_2026_paper.html)]
[[Project](https://ephemeral182.github.io/PosterOmni/)] <br>

**DesignAsCode: Bridging Structural Editability and Visual Fidelity in Graphic Design Generation** <br>
*Ziyuan Liu, Shizhao Sun, Danqing Huang, Yingdong Shi, Meisheng Zhang, Ji Li, Jingsong Yu, Jiang Bian.* <br>
arXiv 2026, School of Software and Microelectronics, Peking University, Beijing, China & Microsoft, Beijing, China & Microsoft, Mountain View, USA & ShanghaiTech University, Shanghai, China & Peking University, Beijing, China <br>
**Graphic Design Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2602.17690)]
[[Project](https://liuziyuan1109.github.io/design-as-code/)] <br>

**APEX: Academic Poster Editing Agentic Expert** <br>
*Chengxin Shi, Qinnan Cai, Zeyuan Chen, Long Zeng, Yibo Zhao, Jing Yu, Jianxiang Yu, Xiang Li.* <br>
arXiv 2026, School of Data Science and Engineering, East China Normal University <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2601.04794)]
[[Github](https://github.com/Breesiu/APEX)] <br>

**PosterVerse: A Full-Workflow Framework for Commercial-Grade Poster Generation with HTML-Based Scalable Typography** <br>
*Junle Liu, Peirong Zhang, Yuyi Zhang, Pengyu Yan, Hui Zhou, Xinyue Zhou, Fengjun Guo, Lianwen Jin.* <br>
AAAI 2026 <br>
**Graphic Design Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2601.03993)]
[[Github](https://github.com/wuhaer/PosterVerse)] <br>

**PSDesigner: Automated Graphic Design with a Human-Like Creative Workflow** <br>
*Xincheng Shuai, Song Tang, Yutong Huang, Henghui Ding, Dacheng Tao.* <br>
CVPR 2026 <br>
**Graphic Design Generation** **LLM-based** [[Paper](https://openaccess.thecvf.com/content/CVPR2026/papers/Shuai_PSDesigner_Automated_Graphic_Design_with_a_Human-Like_Creative_Workflow_CVPR_2026_paper.pdf)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Shuai_PSDesigner_Automated_Graphic_Design_with_a_Human-Like_Creative_Workflow_CVPR_2026_paper.html)] <br>

**Can Vision–Language Models Assess Graphic Design Aesthetics? A Benchmark, Evaluation, and Dataset Perspective.** <br>
*Ruichuan An, Shizhao Sun, Danqing Huang, Mingxi Cheng, Yan Gao, Ji Li, YU QIAO, Jiang Bian.* <br>
ICLR 2026 <br>
**Dataset / Evaluation** [[Paper](https://proceedings.iclr.cc/paper_files/paper/2026/file/844a3c3b8d9bccf0c24dfe07ea59517b-Paper-Conference.pdf)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/844a3c3b8d9bccf0c24dfe07ea59517b-Abstract-Conference.html)] <br>

**AutoPP: Towards Automated Product Poster Generation and Optimization** <br>
*Jiahao Fan, Yuxin Qin, Wei Feng, Yanyin Chen, Yaoyu Li, Ao Ma, Yixiu Li, Li Zhuang, Haoyi Bian, Zheng Zhang, Jingjing Lv, Junjie Shen, Ching Law.* <br>
AAAI 2026 <br>
**Graphic Design Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2512.21921)]
[[Github](https://github.com/JD-GenX/AutoPP)] <br>

**Qwen-Image-Layered: Towards Inherent Editability via Layer Decomposition** <br>
*Shengming Yin, Zekai Zhang, Zecheng Tang, Kaiyuan Gao, Xiao Xu, Kun Yan, Jiahao Li, Yilei Chen, Yuxiang Chen, Heung-Yeung Shum, Lionel M. Ni, Junyang Lin, Chenfei Wu.* <br>
CVPR 2026, HKUST(GZ) Alibaba HKUST <br>
**Graphic Design Editing** [[Paper](https://arxiv.org/abs/2512.15603)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Yin_Qwen-Image-Layered_Towards_Inherent_Editability_via_Layer_Decomposition_CVPR_2026_paper.html)]
[[Github](https://github.com/QwenLM/Qwen-Image-Layered)] <br>

**UniLayDiff: A Unified Diffusion Transformer for Content-Aware Layout Generation** <br>
*Zeyang Liu, Le Wang, Sanping Zhou, Yuxuan Wu, Xiaolong Sun, Gang Hua, Haoxiang Li.* <br>
CVPR 2026 Findings, College of Artificial Intelligence, Xi’an Jiaotong University Amazon.com, Inc. Pixocial Technology <br>
**Content-Aware** [[Paper](https://arxiv.org/abs/2512.08897)] <br>

**SciPostGen: Bridging the Gap between Scientific Papers and Poster Layouts** <br>
*Shun Inadumi, Shohei Tanaka, Tosho Hirasawa, Atsushi Hashimoto, Koichiro Yoshino, Yoshitaka Ushiku.* <br>
CVPR 2026 Findings, OMRON SINIC X Corp & NAIST & The University of Osaka <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2511.22490)]
[[Project](https://omron-sinicx.github.io/paper2layout/)] <br>

**SkyReels-Text: Fine-Grained Font-Controllable Text Editing for Poster Design** <br>
*Yunjie Yu, Jingchen Wu, Junchen Zhu, Chunze Lin, Guibin Chen.* <br>
CVPR 2026, Skywork AI <br>
**Graphic Design Editing** [[Paper](https://arxiv.org/abs/2511.13285)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Yu_SkyReels-Text_Fine-Grained_Font-Controllable_Text_Editing_for_Poster_Design_CVPR_2026_paper.html)]
[[Github](https://github.com/SkyworkAI/SkyReels-Text)] <br>

**OmniDocLayout: Towards Diverse Document Layout Generation via Coarse-to-Fine LLM Learning** <br>
*Hengrui Kang, Zhuangcheng Gu, Zhiyuan Zhao, Zichen Wen, Bin Wang, Weijia Li, Conghui He.* <br>
CVPR 2026, Shanghai Jiao Tong University & Shanghai AI Laboratory & Sun Yat-sen University <br>
**Content-Agnostic** **LLM-based** [[Paper](https://arxiv.org/abs/2510.26213)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2026/html/Kang_OmniDocLayout_Towards_Diverse_Document_Layout_Generation_via_Coarse-to-Fine_LLM_Learning_CVPR_2026_paper.html)]
[[Github](https://github.com/opendatalab/OmniDocLayout)]
[[Dataset](https://huggingface.co/datasets/khr0516/OmniDocLayout-1M)] <br>

**PosterForest: Hierarchical Multi-Agent Collaboration for Scientific Poster Generation** <br>
*Jiho Choi, Seojeong Park, Seongjong Song, Hyunjung Shim.* <br>
ACL 2026 <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2508.21720)] <br>

**PosterGen: Aesthetic-Aware Multi-Modal Paper-to-Poster Generation via Multi-Agent LLMs** <br>
*Zhilin Zhang, Xiang Zhang, Jiaqi Wei, Yiwei Xu, Chenyu You.* <br>
CVPR 2026 Findings, Stony Brook University & New York University & University of British Columbia & Zhejiang University & University of California, Los Angeles <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2508.17188)]
[[Project](https://Y-Research-SBU.github.io/PosterGen)]
[[Github](https://github.com/Y-Research-SBU/PosterGen)] <br>

**PosterCraft: Rethinking High-Quality Aesthetic Poster Generation in a Unified Framework** <br>
*Sixiang Chen, Jianyu Lai, Jialin Gao, Tian Ye, Haoyu Chen, Hengyu Shi, Shitong Shao, Yunlong Lin, Song Fei, Zhaohu Xing, Yeying Jin, Junfeng Luo, Xiaoming Wei, Lei Zhu.* <br>
ICLR 2026, HKUST (Guangzhou) & Meituan & Xiamen University & National University of Singapore & HKUST <br>
**Graphic Design Generation** [[Paper](https://arxiv.org/abs/2506.10741)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/68d88dcd1e1917c74993902073f08e40-Abstract-Conference.html)]
[[Project](https://ephemeral182.github.io/PosterCraft)] <br>

**CreatiDesign: A Unified Multi-Conditional Diffusion Transformer for Creative Graphic Design** <br>
*Hui Zhang, Dexiang Hong, Maoke Yang, Yutao Cheng, Zhao Zhang, Weidong Chen, Jie Shao, Xinglong Wu, Zuxuan Wu, Yu-Gang Jiang.* <br>
ICLR 2026, Institute of Trustworthy Embodied AI, Fudan University & Shanghai Key Laboratory of Multimodal Embodied AI & Bytedance Intelligent Creation & School of Information Science and Technology, University of Science and Technology of China <br>
**Graphic Design Generation** [[Paper](https://arxiv.org/abs/2505.19114)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/b46b78c353f672d83997d4cce5f1b0fb-Abstract-Conference.html)] <br>

**P2P: Automated Paper-to-Poster Generation and Fine-Grained Benchmark** <br>
*Tao Sun, Enhao Pan, Zhengkai Yang, Kaixin Sui, Jiajun Shi, Xianfu Cheng, Tongliang Li, Ge Zhang, Wenhao Huang, Jian Yang, Zhoujun Li.* <br>
ICLR 2026, ByteDance, China & College of Computer Science, Beijing Information Science and Technology University & Shenzhen Intelligent Strong Technology Co.,Ltd <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2505.17104)]
[[Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/1fe6f635fe265292aba3987b5123ae3d-Abstract-Conference.html)]
[[Github](https://github.com/multimodal-art-projection/P2P)] <br>

## 2025

**AutoPresent: Designing Structured Visuals from Scratch** <br>
*Jiaxin Ge, Zora Zhiruo Wang, Xuhui Zhou, Yi-Hao Peng, Sanjay Subramanian, Qinyue Tan, Maarten Sap, Alane Suhr, Daniel Fried, Graham Neubig, Trevor Darrell.* <br>
CVPR 2025, University of California, Berkeley & Carnegie Mellon University <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2501.00912)]
[[Github](https://github.com/para-lost/AutoPresent)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Ge_AutoPresent_Designing_Structured_Visuals_from_Scratch_CVPR_2025_paper.html)] <br>

**UTDesign: A Unified Framework for Stylized Text Editing and Generation in Graphic Design Images** <br>
*Yiming Zhao, Yuanpeng Gao, Yuxuan Luo, Jiwei Duan, Shisong Lin, Longfei Xiong, Zhouhui Lian.* <br>
SIGGRAPH Asia 2025, Wangxuan Institute of Computer Technology, Peking University, Beijing, China & Kingsoft Office, Zhuhai, China & State Key Laboratory of General Artificial Intelligence, Peking University, Beijing, China <br>
**Graphic Design Generation** [[Paper](https://arxiv.org/abs/2512.20479)]
[[Github](https://github.com/ZYM-PKU/UTDesign)] <br>

**Content-Aware Ad Banner Layout Generation with Two-Stage Chain-of-Thought in Vision Language Models** <br>
*Kei Yoshitake, Kento Hosono, Ken Kobayashi, Kazuhide Nakata.* <br>
arXiv 2025, Institute of Science Tokyo & HAKUHODO Technologies Inc <br>
**Content-Aware** **LLM-based** [[Paper](https://arxiv.org/abs/2512.12596)] <br>

**Sketch-to-Layout: Sketch-Guided Multimodal Layout Generation** <br>
*Riccardo Brioschi, Aleksandr Alekseev, Emanuele Nevali, Berkay Döner, Omar El Malki, Blagoj Mitrevski, Leandro Kieliger, Mark Collier, Andrii Maksai, Jesse Berent, Claudiu Musat, Efi Kokiopoulou.* <br>
ICCV 2025 Workshops (HiGen) <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2510.27632)]
[[Github](https://github.com/google-deepmind/sketch_to_layout)] <br>

**StructLayoutFormer:Conditional Structured Layout Generation via Structure Serialization and Disentanglement** <br>
*Xin Hu, Pengfei Xu, Jin Zhou, Hongbo Fu, Hui Huang.* <br>
arXiv 2025 <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2510.26141)]
[[Github](https://github.com/Teagrus/StructLayoutFormer)] <br>

**SEGA: A Stepwise Evolution Paradigm for Content-Aware Layout Generation with Design Prior** <br>
*Haoran Wang, Bo Zhao, Jinghui Wang, Hanzhang Wang, Huan Yang, Wei Ji, Hao Liu, Xinyan Xiao.* <br>
ICCV 2025, Baidu Inc & Nanjing University & Harbin Institute of Technology & Kuaishou Technology <br>
**Content-Aware** **LLM-based** [[Paper](https://arxiv.org/abs/2510.15749)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_SEGA_A_Stepwise_Evolution_Paradigm_for_Content-Aware_Layout_Generation_with_ICCV_2025_paper.html)]
[[Project](https://brucew91.github.io/SEGA.github.io/)]
[[Github](https://github.com/BruceW91/SEGA)]
[[Dataset](https://github.com/BruceW91/SEGA/tree/main/GenPoster-100K_Dataset)] <br>

**LayerD: Decomposing Raster Graphic Designs into Layers** <br>
*Tomoyuki Suzuki, Kang-Jun Liu, Naoto Inoue, Kota Yamaguchi.* <br>
ICCV 2025, CyberAgent & Tohoku University <br>
**Graphic Design Editing** [[Paper](https://arxiv.org/abs/2509.25134)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Suzuki_LayerD_Decomposing_Raster_Graphic_Designs_into_Layers_ICCV_2025_paper.html)]
[[Project](https://cyberagentailab.github.io/LayerD/)]
[[Github](https://github.com/CyberAgentAILab/LayerD)] <br>

**LLMs as Layout Designers: Enhanced Spatial Reasoning for Content-Aware Layout Generation** <br>
*Sha Li, Stefano Petrangeli, Yu Shen, Xiang Chen, Naren Ramakrishnan.* <br>
arXiv 2025 <br>
**Content-Aware** **LLM-based** [[Paper](https://arxiv.org/abs/2509.16891)] <br>

**SheetDesigner: MLLM-Powered Spreadsheet Layout Generation with Rule-Based and Vision-Based Reflection** <br>
*Qin Chen, Yuanyi Ren, Xiaojun Ma, Mugeng Liu, Han Shi, Dongmei Zhang.* <br>
EMNLP 2025, Peking University & Microsoft <br>
**Document / UI Layout** **LLM-based** [[Paper](https://arxiv.org/abs/2509.07473)]
[[Github](https://github.com/Cqkkkkkk/SheetDesigner)] <br>

**LayoutRectifier: An Optimization-based Post-processing for Graphic Design Layout Generation** <br>
*I-Chao Shen, Ariel Shamir, Takeo Igarashi.* <br>
Pacific Graphics 2025, The University of Tokyo & Reichman University <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2508.11177)]
[[Project](https://jdily.github.io/layoutrectifier.github.io/)] <br>

**Uni-Layout: Integrating Human Feedback in Unified Layout Generation and Evaluation** <br>
*Shuo Lu, Yanyin Chen, Wei Feng, Jiahao Fan, Fengheng Li, Zheng Zhang, Jingjing Lv, Junjie Shen, Ching Law, Jian Liang.* <br>
ACMMM 2025, NLPR & MAIS, CASIA; School of AI, UCAS, Beijing, China & JD.COM, Beijing, China <br>
**Content-Aware** **LLM-based** [[Paper](https://arxiv.org/abs/2508.02374)]
[[Github](https://github.com/JD-GenX/Uni-Layout)] <br>

**IdeaBlocks: Expressing and Reusing Divergent Intents for Graphic Design Exploration using Generative AI** <br>
*DaEun Choi, Kihoon Son, Jaesang Yu, Hyunjoon Jung, Juho Kim.* <br>
arXiv 2025, KAIST, Daejeon, Republic of Korea & MPhora.ai, San Francisco, CA, United States & School of Computing, KAIST, Daejeon, Republic of Korea & SkillBench, Santa Barbara, CA, USA <br>
**Graphic Design Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2507.22163)] <br>

**PosterMate: Audience-driven Collaborative Persona Agents for Poster Design** <br>
*Donghoon Shin, Daniel Lee, Gary Hsieh, Gromit Yeuk-Yin Chan.* <br>
UIST 2025, University of Washington, Seattle, WA, USA & Adobe Inc., San Jose, CA, USA & Adobe Research, San Jose, CA, USA <br>
**Graphic Design Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2507.18572)] <br>

**IGD: Instructional Graphic Design with Multimodal Layer Generation** <br>
*Yadong Qu, Shancheng Fang, Yuxin Wang, Xiaorui Wang, Zhineng Chen, Hongtao Xie, Yongdong Zhang.* <br>
ICCV 2025, University of Science and Technology of China & YuanShi Technology & Institute of Trustworthy Embodied AI, Fudan University <br>
**Graphic Design Generation** [[Paper](https://arxiv.org/abs/2507.09910)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Qu_IGD_Instructional_Graphic_Design_with_Multimodal_Layer_Generation_ICCV_2025_paper.html)] <br>

**Rethinking Layered Graphic Design Generation with a Top-Down Approach** <br>
*Jingye Chen, Zhaowen Wang, Nanxuan Zhao, Li Zhang, Difan Liu, Jimei Yang, Qifeng Chen.* <br>
ICCV 2025, HKUST & Adobe Research & Runway <br>
**Graphic Design Generation** [[Paper](https://arxiv.org/abs/2507.05601)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Rethinking_Layered_Graphic_Design_Generation_with_a_Top-Down_Approach_ICCV_2025_paper.html)] <br>

**ReLayout: Integrating Relation Reasoning for Content-aware Layout Generation with Multi-modal Large Language Models** <br>
*Jiaxu Tian, Xuehui Yu, Yaoxing Wang, Pan Wang, Guangqian Guo, Shan Gao.* <br>
arXiv 2025 <br>
**Content-Aware** **LLM-based** [[Paper](https://arxiv.org/abs/2507.05568)]
[[Dataset](https://huggingface.co/datasets/jiaxutian/ReLayout)] <br>

**DreamPoster: A Unified Framework for Image-Conditioned Generative Poster Design** <br>
*Xiwei Hu, Haokun Chen, Zhongqi Qi, Hui Zhang, Dexiang Hong, Jie Shao, Xinglong Wu.* <br>
arXiv 2025 <br>
**Graphic Design Generation** [[Paper](https://arxiv.org/abs/2507.04218)]
[[Project](https://dreamposter.github.io/)] <br>

**CAL-RAG: Retrieval-Augmented Multi-Agent Generation for Content-Aware Layout Design** <br>
*Najmeh Forouzandehmehr, Reza Yousefi Maragheh, Sriram Kollipara, Kai Zhao, Topojoy Biswas, Evren Korpeoglu, Kannan Achan.* <br>
arXiv 2025, Walmart Global Tech <br>
**Content-Aware** **LLM-based** [[Paper](https://arxiv.org/abs/2506.21934)] <br>

**CreatiPoster: Towards Editable and Controllable Multi-Layer Graphic Design Generation** <br>
*Dexiang Hong, Zhao Zhang, Weidong Chen, Yutao Cheng, Maoke Yang, Gonglei Shi, Hui Zhang, Zhendong Mao.* <br>
arXiv 2025, University of Science and Technology of China, Hefei, China & Intelligent Creation & Fudan University, Shanghai, China <br>
**Graphic Design Generation** [[Paper](https://arxiv.org/abs/2506.10890)]
[[Github](https://github.com/graphic-design-ai/creatiposter)] <br>

**SlideCoder: Layout-aware RAG-enhanced Hierarchical Slide Generation from Design** <br>
*Wenxin Tang, Jingyu Xiao, Wenxuan Jiang, Xi Xiao, Yuhang Wang, Xuxin Tang, Qing Li, Yuehe Ma, Junliang Liu, Shisong Tang, Michael R. Lyu.* <br>
arXiv 2025, Tsinghua University & The Chinese University of Hong Kong & Northeastern University & Southwest University & Kuaishou Technology & Peng Cheng Laboratory & BNU-HKBU United International College & Dalian Maritime University <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2506.07964)]
[[Github](https://github.com/vinsontang1/SlideCoder)] <br>

**LayoutRAG: Retrieval-Augmented Model for Content-agnostic Conditional Layout Generation** <br>
*Yuxuan Wu, Le Wang, Sanping Zhou, Mengnan Liu, Gang Hua, Haoxiang Li.* <br>
arXiv 2025, Xi’an Jiaotong University & Amazon.com, Inc & Pixocial Technology <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2506.02697)] <br>

**Paper2Poster: Towards Multimodal Poster Automation from Scientific Papers** <br>
*Wei Pang, Kevin Qinghong Lin, Xiangru Jian, Xi He, Philip H.S. Torr.* <br>
NeurIPS 2025, University of Waterloo & University of Oxford & Vector Institute <br>
**Scientific Poster / Slide Generation** **LLM-based** [[Paper](https://arxiv.org/abs/2505.21497)]
[[Proceedings](https://papers.neurips.cc/paper_files/paper/2025/hash/17337b1d5eeac8b59c80e025a552fa7a-Abstract-Datasets_and_Benchmarks_Track.html)]
[[Github](https://github.com/Paper2Poster/Paper2Poster)]
[[Project](https://paper2poster.github.io)] <br>

**Scan-and-Print: Patch-level Data Summarization and Augmentation for Content-aware Layout Generation in Poster Design** <br>
*HsiaoYuan Hsu, Yuxin Peng.* <br>
arXiv 2025, Wangxuan Institute of Computer Technology, Peking University <br>
**Content-Aware** [[Paper](https://arxiv.org/abs/2505.20649)]
[[Project](https://thekinsley.github.io/Scan-and-Print/)] <br>

**Aggregated Structural Representation with Large Language Models for Human-Centric Layout Generation** <br>
*Jiongchao Jin, Shengchu Zhao, Dajun Chen, Wei Jiang, Yong Li.* <br>
arXiv 2025, Ant Group & Agency for Science, Technology and Research <br>
**Content-Agnostic** **LLM-based** [[Paper](https://arxiv.org/abs/2505.19554)] <br>

**PosterO: Structuring Layout Trees to Enable Language Models in Generalized Content-Aware Layout Generation** <br>
*HsiaoYuan Hsu, Yuxin Peng.* <br>
CVPR 2025, Wangxuan Institute of Computer Technology, Peking University <br>
**Content-Aware** [[Paper](https://arxiv.org/abs/2505.07843)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Hsu_PosterO_Structuring_Layout_Trees_to_Enable_Language_Models_in_Generalized_CVPR_2025_paper.html)]
[[Project](https://thekinsley.github.io/PosterO/)] <br>

**Generating Animated Layouts as Structured Text Representations** <br>
*Yeonsang Shin, Jihwan Kim, Yumin Song, Kyungseung Lee, Hyunhee Chung, Taeyoung Na.* <br>
CVPR 2025 Workshops (AI4CC), Seoul National University & SK telecom <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2505.00975)]
[[Project](https://yeonsangshin.github.io/projects/Vaker)] <br>

**GraphicBench: A Planning Benchmark for Graphic Design with Language Agents** <br>
*Dayeon Ki, Tianyi Zhou, Marine Carpuat, Gang Wu, Puneet Mathur, Viswanathan Swaminathan.* <br>
arXiv 2025, University of Maryland, College Park & Adobe Research <br>
**Dataset / Evaluation** [[Paper](https://arxiv.org/abs/2504.11571)] <br>

**LayoutCoT: Unleashing the Deep Reasoning Potential of Large Language Models for Layout Generation** <br>
*Hengyu Shi, Junhao Su, Tianyang Han, Junfeng Luo, Jialin Gao.* <br>
arXiv 2025, Meituan <br>
**Content-Agnostic** **LLM-based** [[Paper](https://arxiv.org/abs/2504.10829)] <br>

**PosterMaker: Towards High-Quality Product Poster Generation with Accurate Text Rendering** <br>
*Yifan Gao, Zihang Lin, Chuanbin Liu, Min Zhou, Tiezheng Ge, Bo Zheng, Hongtao Xie.* <br>
CVPR 2025, University of Science and Technology of China & Taobao & Tmall Group of Alibaba <br>
**Graphic Design Generation** [[Paper](https://arxiv.org/abs/2504.06632)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Gao_PosterMaker_Towards_High-Quality_Product_Poster_Generation_with_Accurate_Text_Rendering_CVPR_2025_paper.html)]
[[Project](https://poster-maker.github.io)] <br>

**From Fragment to One Piece: A Survey on AI-Driven Graphic Design** <br>
*Xingxing Zou, Wen Zhang, Nanxuan Zhao.* <br>
arXiv 2025, The Hong Kong Polytechnic University & Snap Inc. & Adobe <br>
**Survey** [[Paper](https://arxiv.org/abs/2503.18641)] <br>

**AesthetiQ: Enhancing Graphic Layout Design via Aesthetic-Aware Preference Alignment of Multi-modal Large Language Models** <br>
*Sohan Patnaik, Rishabh Jain, Balaji Krishnamurthy, Mausoom Sarkar.* <br>
CVPR 2025, MDSR Adobe <br>
**Content-Aware** **LLM-based** [[Paper](https://arxiv.org/abs/2503.00591)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Patnaik_AesthetiQ_Enhancing_Graphic_Layout_Design_via_Aesthetic-Aware_Preference_Alignment_of_CVPR_2025_paper.html)] <br>

**T-Stars-Poster: A Framework for Product-Centric Advertising Image Design** <br>
*Hongyu Chen, Min Zhou, Jing Jiang, Jiale Chen, Yang Lu, Zihang Lin, Bo Xiao, Tiezheng Ge, Bo Zheng.* <br>
arXiv 2025, Alibaba Group, Beijing, China & Beijing University of Posts and Telecommunications, Beijing, China & Beijing, China <br>
**Graphic Design Generation** [[Paper](https://arxiv.org/abs/2501.14316)]
[[Github](https://github.com/alimama-creative/PITA-dataset)] <br>

**From Elements to Design: A Layered Approach for Automatic Graphic Design Composition** <br>
*Jiawei Lin, Shizhao Sun, Danqing Huang, Ting Liu, Ji Li, Jiang Bian.* <br>
CVPR 2025 <br>
**Graphic Design Generation** [[Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Lin_From_Elements_to_Design_A_Layered_Approach_for_Automatic_Graphic_CVPR_2025_paper.pdf)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_From_Elements_to_Design_A_Layered_Approach_for_Automatic_Graphic_CVPR_2025_paper.html)] <br>

**SKE-Layout: Spatial Knowledge Enhanced Layout Generation with LLMs** <br>
*Junsheng Wang, Nieqing Cao, Yan Ding, Mengying Xie, Fuqiang Gu, Chao Chen.* <br>
CVPR 2025 <br>
**Content-Agnostic** **LLM-based** [[Paper](https://openaccess.thecvf.com/content/CVPR2025/papers/Wang_SKE-Layout_Spatial_Knowledge_Enhanced_Layout_Generation_with_LLMs_CVPR_2025_paper.pdf)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_SKE-Layout_Spatial_Knowledge_Enhanced_Layout_Generation_with_LLMs_CVPR_2025_paper.html)] <br>

**Lay-Your-Scene: Natural Scene Layout Generation with Diffusion Transformers** <br>
*Divyansh Srivastava, Xiang Zhang, He Wen, Chenru Wen, Zhuowen Tu.* <br>
ICCV 2025 <br>
**Scene Layout Generation** [[Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/Srivastava_Lay-Your-Scene_Natural_Scene_Layout_Generation_with_Diffusion_Transformers_ICCV_2025_paper.pdf)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/Srivastava_Lay-Your-Scene_Natural_Scene_Layout_Generation_with_Diffusion_Transformers_ICCV_2025_paper.html)] <br>

**PlanGen: Towards Unified Layout Planning and Image Generation in Auto-Regressive Vision Language Models** <br>
*Runze He, Bo Cheng, Yuhang Ma, Qingxiang Jia, Shanyuan Liu, Ao Ma, Xiaoyu Wu, Liebucha Wu, Dawei Leng, Yuhui Yin.* <br>
ICCV 2025 <br>
**Graphic Design Generation** **LLM-based** [[Paper](https://openaccess.thecvf.com/content/ICCV2025/papers/He_PlanGen_Towards_Unified_Layout_Planning_and_Image_Generation_in_Auto-Regressive_ICCV_2025_paper.pdf)]
[[Proceedings](https://openaccess.thecvf.com/content/ICCV2025/html/He_PlanGen_Towards_Unified_Layout_Planning_and_Image_Generation_in_Auto-Regressive_ICCV_2025_paper.html)] <br>

**POSTA: A Go-to Framework for Customized Artistic Poster Generation** <br>
*Haoyu Chen, Xiaojie Xu, Wenbo Li, Jingjing Ren, Tian Ye, Songhua Liu, Ying-Cong Chen, Lei Zhu, Xinchao Wang.* <br>
CVPR 2025, HKUST(Guangzhou) & CUHK & NUS & HKUST <br>
**LLM-based** [[Paper](https://arxiv.org/abs/2503.14908)]
[[Project](https://haoyuchen.com/POSTA)]
[[Proceedings](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_POSTA_A_Go-to_Framework_for_Customized_Artistic_Poster_Generation_CVPR_2025_paper.html)] <br>

**Smaller But Better: Unifying Layout Generation with Smaller Large Language Models** <br>
*Peirong Zhang, Jiaxin Zhang, Jiahuan Cao, Hongliang Li, Lianwen Jin.* <br>
arXiv 2025, South China University of Technology <br>
**Content-Agnostic** **LLM-based** [[Paper](https://arxiv.org/abs/2502.14005)]
[[Github](https://github.com/NiceRingNode/LGGPT)] <br>

**Illuminating Spaces: Deep Reinforcement Learning and Laser-Wall Partitioning for Architectural Layout Generation** <br>
*Reza Kakooee, Benjamin Dillenburger.* <br>
arXiv 2025, ETH Zurich <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2502.04407)] <br>

**Problem Solved? Information Extraction Design Space for Layout-Rich Documents using LLMs** <br>
*Gaye Colakoglu, Gürkan Solmaz, Jonathan Fürst.* <br>
arXiv 2025, Zurich University of Applied Sciences <br>
**layout-aware**  **LLM-based** [[Paper](https://arxiv.org/abs/2502.18179)]
[[Github](https://github.com/gayecolakoglu/LayIE-LLM)] <br>

**Spatial Information Integration in Small Language Models for Document Layout Generation and Classification** <br>
*Pablo Melendez, Clemens Havas.* <br>
arXiv 2025, Salzburg University of Applied Sciences<br>
**Content-Agnostic** **LLM-based** [[Paper](https://arxiv.org/abs/2501.05497)] <br>

**GLDesigner: Leveraging Multi-Modal LLMs as Designer for Enhanced Aesthetic Text Glyph Layouts** <br>
*Junwen He, Yifan Wang, Lijun Wang, Huchuan Lu, Jun-Yan He, Chenyang Li, Hanyuan Chen, Jin-Peng Lan, Bin Luo, Yifeng Geng.* <br>
ACMMM 2025, Dalian University of Technology & Alibaba <br>
[[Paper](https://arxiv.org/abs/2411.11435)] <br>

**Multimodal Markup Document Models for Graphic Design Completion** <br>
*Kotaro Kikuchi, Naoto Inoue, Mayu Otani, Edgar Simo-Serra, Kota Yamaguchi.* <br>
ACMMM 2025, CyberAgent & Waseda University <br>
**Content-Aware** [[Paper](https://arxiv.org/abs/2409.19051)]
[[Project](https://cyberagentailab.github.io/MarkupDM/)] <br>

**GlyphDraw2: Automatic Generation of Complex Glyph Posters with Diffusion Models and Large Language Models** <br>
*Jian Ma, Yonglin Deng, Chen Chen, Haonan Lu, Zhenyu Yang.* <br>
AAAI 2025, OPPO AI Center & CUHK Shenzhen <br>
**LLM-based** [[Paper](https://arxiv.org/abs/2407.02252)]
[[Github](https://github.com/OPPO-Mente-Lab/GlyphDraw2)] <br>

## 2024

**VASCAR: Content-Aware Layout Generation via Visual-Aware Self-Correction** <br>
*Jiahao Zhang, Ryota Yoshihashi, Shunsuke Kitada, Atsuki Osanai, Yuta Nakashima.* <br>
arXiv 2024, Osaka University <br>
**Content-Aware** **LLM-based** [[Paper](https://arxiv.org/abs/2412.04237)] <br>

**DogLayout: Denoising Diffusion GAN for Discrete and Continuous Layout Generation** <br>
*Zhaoxing Gan, Guangnan Ye.* <br>
arXiv 2024, Fudan University <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2412.00381)]
[[Github](https://github.com/deadsmither5/DogLayout)] <br>

**Image-aware layout generation with user constraints for poster design** <br>
*Chenchen Xu, Kaixin Han, Weiwei Xu.* <br>
The Visual Computer, Zhejiang University <br>
**Content-Aware** [[Paper](https://link.springer.com/article/10.1007/s00371-024-03657-z)] <br>

**Design Element Aware Poster Layout Generation** <br>
*Yinan Li, Jia Chen, Yin Bai, Jia Cheng, Jun Lei.* <br>
CIKM 2024, Mtituan <br>
**Content-Aware** [[Paper](https://dl.acm.org/doi/abs/10.1145/3627673.3679557)] <br>

**Layout-Corrector: Alleviating Layout Sticking Phenomenon in Discrete Diffusion Model** <br>
*Shoma Iwai, Atsuki Osanai, Shunsuke Kitada, Shinichiro Omachi.* <br>
ECCV 2024, Tohoku University & LY Corporation <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2409.16689)]
[[Project](https://iwa-shi.github.io/Layout-Corrector-Project-Page/)] <br>

**LTSim: Layout Transportation-based Similarity Measure for Evaluating Layout Generation** <br>
*Mayu Otani, Naoto Inoue, Kotaro Kikuchi, Riku Togashi.* <br>
arXiv 2024, CyberAgent <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2407.12356)] <br>

**LayoutDiT: Exploring Content-Graphic Balance in Layout Generation with Diffusion Transformer** <br>
*Yu Li, Yifan Chen, Gongye Liu, Fei Yin, Qingyan Bai, Jie Wu, Hongfa Wang, Ruihang Chu, Yujiu Yang.* <br>
arXiv 2024, Tsinghua University & Tencent & HKUST <br>
**Content-Aware** [[Paper](https://arxiv.org/abs/2407.15233)] <br>

**SciPostLayout: A Dataset for Layout Analysis and Layout Generation of Scientific Posters** <br>
*Shohei Tanaka, Hao Wang, Yoshitaka Ushiku.* <br>
BMVC 2024, OMRON SINIC X Corporation & Waseda University <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2407.19787)] [[Github](https://github.com/omron-sinicx/scipostlayout)]
[[Dataset](https://huggingface.co/datasets/omron-sinicx/scipostlayout_v2)] <br>

**Predicting Visual Attention in Graphic Design Documents** <br>
*Souradeep Chakraborty, Zijun Wei, Conor Kelton, Seoyoung Ahn, Aruna Balasubramanian, Gregory J. Zelinsky, Dimitris Samaras.* <br>
arXiv 2024, Stony Brook University <br>
[[Paper](https://arxiv.org/pdf/2407.02439)] <br>

**Glyph-ByT5-v2: A Strong Aesthetic Baseline for Accurate Multilingual Visual Text Rendering** <br>
*Zeyu Liu, Weicong Liang, Yiming Zhao, Bohan Chen, Lin Liang, Lijuan Wang, Ji Li, Yuhui Yuan.* <br>
arXiv 2024, Microsoft <br>
[[Paper](https://arxiv.org/abs/2406.10208)]
[[Project](https://glyph-byt5-v2.github.io)]
[[Github](https://github.com/AIGText/Glyph-ByT5)] <br>

**OpenCOLE: Towards Reproducible Automatic Graphic Design Generation** <br>
*Naoto Inoue, Kento Masui, Wataru Shimoda, Kota Yamaguchi.* <br>
CVPR 2024 Workshops, CyberAgent <br>
[[Paper](https://arxiv.org/abs/2406.08232)]
[[Github](https://github.com/CyberAgentAILab/OpenCOLE)] <br>

**PosterLLaVa: Constructing a Unified Multi-modal Layout Generator with LLM** <br>
*Tao Yang, Yingmin Luo, Zhongang Qi, Yang Wu, Ying Shan, Chang Wen Chen.* <br>
arXiv 2024, Tencent PCG <br>
**Content-Aware** **LLM-based** [[Paper](https://arxiv.org/abs/2406.02884)]
[[Project](https://huggingface.co/spaces/posterllava/PosterLLaVA)]
[[Github](https://github.com/posterllava/PosterLLaVA)] <br>

**CoLay: Controllable Layout Generation through Multi-conditional Latent Diffusion** <br>
*Chin-Yi Cheng, Ruiqi Gao, Forrest Huang, Yang Li.* <br>
arXiv 2024, Google Research <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2405.13045)] <br>

**Leveraging Human Revisions for Improving Text-to-Layout Models** <br>
*Amber Xie, Chin-Yi Cheng, Forrest Huang, Yang Li.* <br>
arXiv 2024, Google Research <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2405.13026)] <br>

**Automatic Layout Planning for Visually-Rich Documents with Instruction-Following Models** <br>
*Wanrong Zhu, Jennifer Healey, Ruiyi Zhang, William Yang Wang, Tong Sun.* <br>
arXiv 2024, Adobe & UC Santa Barbara <br>
**LLM-based** [[Paper](https://arxiv.org/abs/2404.15271)] <br>

**Graphic Design with Large Multimodal Model** <br>
*Yutao Cheng, Zhao Zhang, Maoke Yang, Hui Nie, Chunyuan Li, Xinglong Wu, Jie Shao.* <br>
arXiv 2024, ByteDance & UCAS <br>
**LLM-based** **HLG** [[Paper](https://arxiv.org/abs/2404.14368)]
[[Github](https://github.com/graphic-design-ai/graphist)] <br>

**PosterLlama: Bridging Design Ability of Langauge Model to Contents-Aware Layout Generation** <br>
*Jaejung Seol, Seojun Kim, Jaejun Yoo.* <br>
ECCV 2024, Ulsan National Institute of Science and Technology <br>
**LLM-based** [[Paper](https://arxiv.org/abs/2404.00995)]
[[Github-1](https://github.com/jaepoong/PosterLlama)]
[[Github-2](https://anonymous.4open.science/r/PosterLlama/readme.md)]<br>

**Constrained Layout Generation with Factor Graphs** <br>
*Mohammed Haroon Dupty, Yanfei Dong, Sicong Leng, Guoji Fu, Yong Liang Goh, Wei Lu, Wee Sun Lee.* <br>
CVPR 2024, PayPal & National University of Singapore <br>
[[Paper](https://arxiv.org/abs/2404.00385)] <br>

**LayoutFlow: Flow Matching for Layout Generation** <br>
*Julian Jorge Andrade Guerreiro, Naoto Inoue, Kento Masui, Mayu Otani, Hideki Nakayama.* <br>
ECCV 2024, CyberAgent & The University of Tokyo <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2403.18187)]
[[Project](https://julianguerreiro.github.io/layoutflow/)]
[[Github](https://github.com/JulianGuerreiro/LayoutFlow)] <br>

**Glyph-ByT5: A Customized Text Encoder for Accurate Visual Text Rendering** <br>
*Zeyu Liu, Weicong Liang, Zhanhao Liang, Chong Luo, Ji Li, Gao Huang, Yuhui Yuan.* <br>
ECCV 2024, Microsoft Research Asia & Tsinghua University <br>
[[Paper](https://arxiv.org/abs/2403.09622)]
[[Project](https://glyph-byt5.github.io)]
[[Github](https://github.com/AIGText/Glyph-ByT5)] <br>

**Visual Layout Composer: Image-Vector Dual Diffusion Model for Design Layout Generation** <br>
*Mohammad Amin Shabani, Zhaowen Wang, Difan Liu, Nanxuan Zhao, Jimei Yang, Yasutaka Furukawa.* <br>
CVPR 2024, Adobe & Simon Fraser University <br>
**Content-Aware** [[Paper](https://aminshabani.github.io/visual_layout_composer/pdfs/visual_layout_composer.pdf)]
[[Project](https://aminshabani.github.io/visual_layout_composer/)] <br>

**Desigen: A Pipeline for Controllable Design Template Generation** <br>
*Haohan Weng, Danqing Huang, Yu Qiao, Zheng Hu, Chin-Yew Lin, Tong Zhang, C. L. Philip Chen.* <br>
CVPR 2024, Microsoft Research Asia & South China University of Technology <br>
[[Paper](https://arxiv.org/abs/2403.09093)]
[[Github](https://github.com/whaohan/desigen)]
[[Project](https://whaohan.github.io/desigen)] <br>

**Retrieval-Augmented Layout Transformer for Content-Aware Layout Generation** <br>
*Daichi Horita, Naoto Inoue, Kotaro Kikuchi, Kota Yamaguchi, Kiyoharu Aizawa.* <br>
CVPR 2024(oral), CyberAgent & The University of Tokyo <br>
**Content-Aware** [[Paper](https://arxiv.org/abs/2311.13602)]
[[Project](https://udonda.github.io/RALF/)]
[[Github](https://github.com/CyberAgentAILab/RALF)] <br>

**LayoutNUWA: Revealing the Hidden Layout Expertise of Large Language Models** <br>
*Zecheng Tang, Chenfei Wu, Juntao Li, Nan Duan.* <br>
ICLR 2024, Microsoft Research Asia & Soochow University <br>
**Content-Agnostic** [[Paper](https://openreview.net/pdf?id=qCUWVT0Ayy)]
[[Github](https://github.com/ProjectNUWA/LayoutNUWA)] <br>

**Towards Aligned Layout Generation via Diffusion Model with Aesthetic Constraints** <br>
*Jian Chen, Ruiyi Zhang, Yufan Zhou, Rajiv Jain, Zhiqiang Xu, Ryan Rossi, Changyou Chen.* <br>
ICLR 2024, Adobe Research & MBZUAI & University at Buffalo <br>
**Content-Agnostic** [[Paper](https://openreview.net/pdf?id=kJ0qp9Xdsh)]
[[Github](https://github.com/puar-playground/lace)] <br>

**Spot the Error: Non-autoregressive Graphic Layout Generation with Wireframe Locator** <br>
*Jieru Lin, Danqing Huang, Tiejun Zhao, Dechen Zhan, Chin-Yew Lin.* <br>
AAAI 2024, Microsoft Research & Harbin Institute of Technology <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2401.16375)]
[[Github](https://github.com/ffffatgoose/SpotError)] <br>

**Dolfin: Diffusion Layout Transformers without Autoencoder** <br>
*Yilin Wang, Zeyuan Chen, Liangjun Zhong, Zheng Ding, Zhizhou Sha, Zhuowen Tu.* <br>
ECCV 2024, Tsinghua University & University of California, San Diego <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2310.16305)] <br>

**LayoutDETR: Detection Transformer Is a Good Multimodal Layout Designer** <br>
*Ning Yu, Chia-Chih Chen, Zeyuan Chen, Rui Meng, Gang Wu, Paul Josel, Juan Carlos Niebles, Caiming Xiong, Ran Xu.* <br>
ECCV 2024, Salesforce Research <br>
**Content-Aware** [[Paper](https://arxiv.org/abs/2212.09877)]
[[Github](https://github.com/salesforce/LayoutDETR)] <br>

## 2023

**COLE: A Hierarchical Generation Framework for Multi-Layered and Editable Graphic Design** <br>
*Peidong Jia, Chenxuan Li, Yuhui Yuan, Zeyu Liu, Yichao Shen, Bohan Chen, Xingru Chen, Yinglin Zheng, Dong Chen, Ji Li, Xiaodong Xie, Shanghang Zhang, Baining Guo.* <br>
arXiv 2023, Microsoft Research Asia & Peking University <br>
[[Paper](https://arxiv.org/abs/2311.16974)] <br>

**Relation-Aware Diffusion Model for Controllable Poster Layout Generation** <br>
*Fengheng Li, An Liu, Wei Feng, Honghe Zhu, Yaoyu Li, Zheng Zhang, Jingjing Lv, Xin Zhu, Junjie Shen, Zhangang Lin, Jingping Shao.* <br>
CIKM 2023, JD & Nankai University <br>
**Content-Aware** [[Paper](https://arxiv.org/abs/2306.09086)]
[[Github](https://github.com/liuan0803/RADM?tab=readme-ov-file)]
[[Dataset](https://github.com/liuan0803/RADM?tab=readme-ov-file)] <br>

**LayoutPrompter: Awaken the Design Ability of Large Language Models**
*Jiawei Lin, Jiaqi Guo, Shizhao Sun, Zijiang James Yang, Jian-Guang Lou, Dongmei Zhang.* <br>
NeurIPS 2023, Microsoft Research Asia & Shanghai Jiao Tong University <br>
**LLM-based** [[Paper](https://proceedings.neurips.cc/paper_files/paper/2023/file/88a129e44f25a571ae8b838057c46855-Paper-Conference.pdf)]
[[Github](https://github.com/microsoft/LayoutGeneration)] <br>

**LayoutGPT: Compositional Visual Planning and Generation with Large Language Models** <br>
*Weixi Feng, Wanrong Zhu, Tsu-jui Fu, Varun Jampani, Arjun Akula, Xuehai He, Sugato Basu, Xin Eric Wang, William Yang Wang.* <br>
NeurIPS 2023, Google & UC Santa Barbara <br>
**LLM-based** [[Paper](https://arxiv.org/abs/2305.15393)]
[[Project](https://layoutgpt.github.io)]
[[Github](https://github.com/weixi-feng/LayoutGPT)] <br>

**DLT: Conditioned layout generation with Joint Discrete-Continuous Diffusion Layout Transformer** <br>
*Elad Levi, Eli Brosh, Mykola Mykhailych, Meir Perez.* <br>
ICCV 2023, Wix.com <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2303.03755)]
[[Project](https://wix-incubator.github.io/DLT/)]
[[Github](https://github.com/wix-incubator/DLT)] <br>

**LayoutDiffusion: Improving Graphic Layout Generation by Discrete Diffusion Probabilistic Models** <br>
*Junyi Zhang, Jiaqi Guo, Shizhao Sun, Jian-Guang Lou, Dongmei Zhang.* <br>
ICCV 2023, Microsoft Research Asia & Shanghai Jiao Tong University <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2303.11589)]
[[Github](https://github.com/microsoft/LayoutGeneration)]
[[Project](https://layoutdiffusion.github.io)] <br>

**A Parse-Then-Place Approach for Generating Graphic Layouts from Textual Descriptions** <br>
*Jiawei Lin, Jiaqi Guo, Shizhao Sun, Weijiang Xu, Ting Liu.* <br>
ICCV 2023, Microsoft Research Asia & Shanghai Jiao Tong University <br>
**Content-Agnostic** [[Paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Lin_A_Parse-Then-Place_Approach_for_Generating_Graphic_Layouts_from_Textual_Descriptions_ICCV_2023_paper.pdf)]
[[Github](https://github.com/microsoft/LayoutGeneration)] <br>

**Diffusion-based Document Layout Generation** <br>
*Liu He, Yijuan Lu, John Corring, Dinei Florencio, Cha Zhang.* <br>
ICDAR 2023, Microsoft Cloud and AI & Purdue University <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2303.10787)] <br>

**PLay: Parametrically Conditioned Layout Generation using Latent Diffusion** <br>
*Chin-Yi Cheng, Forrest Huang, Gang Li, Yang Li.* <br>
ICML 2023, Google Research <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2301.11529v2)] <br>

**PosterLayout: A New Benchmark and Approach for Content-aware Visual-Textual Presentation Layout** <br>
*HsiaoYuan Hsu, Xiangteng He, Yuxin Peng, Hao Kong, Qing Zhang.* <br>
CVPR 2023, Meituan & Peking University <br>
**Content-Aware** [[Paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Hsu_PosterLayout_A_New_Benchmark_and_Approach_for_Content-Aware_Visual-Textual_Presentation_CVPR_2023_paper.pdf)]
[[Project](http://39.108.48.32/mipl/PosterLayout/)]
[[Github](https://github.com/PKU-ICST-MIPL/PosterLayout-CVPR2023)]
[[Dataset1](http://39.108.48.32/mipl/PosterLayout/)]
[[Dataset2](https://huggingface.co/datasets/creative-graphic-design/PKU-PosterLayout)] <br>

**LayoutDM: Transformer-based diffusion model for layout generation** <br>
*Shang Chai, Liansheng Zhuang, Fengying Yan.* <br>
CVPR 2023, University of Science and Technology of China & Tianjin University <br>
**Content-Agnostic** [[Paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Chai_LayoutDM_Transformer-Based_Diffusion_Model_for_Layout_Generation_CVPR_2023_paper.pdf)] <br>

**LayoutDM: Discrete Diffusion Model for Controllable Layout Generation** <br>
*Naoto Inoue, Kotaro Kikuchi, Edgar Simo-Serra, Mayu Otani, Kota Yamaguchi.* <br>
CVPR 2023, CyberAgent & Waseda University <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2303.08137)]
[[Project](https://cyberagentailab.github.io/layout-dm)]
[[Github](https://github.com/CyberAgentAILab/layout-dm)] <br>

**LayoutFormer++: Conditional Graphic Layout Generation via Constraint Serialization and Decoding Space Restriction** <br>
*Zhaoyun Jiang, Jiaqi Guo, Shizhao Sun, Huayu Deng, Zhongkai Wu, Vuksan Mijovic, Zijiang James Yang, Jian-Guang Lou, Dongmei Zhang.* <br>
CVPR 2023, Microsoft Research Asi & Xi’an Jiaotong University <br>
**Content-Agnostic** [[Paper](http://arxiv.org/abs/2208.08037)]
[[Github](https://github.com/microsoft/LayoutGeneration)] <br>

**Towards Flexible Multi-modal Document Models** <br>
*Naoto Inoue, Kotaro Kikuchi, Edgar Simo-Serra, Mayu Otani, Kota Yamaguchi.* <br>
CVPR 2023, CyberAgent & Waseda University <br>
**Content-Agnostic** [[Paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Inoue_Towards_Flexible_Multi-Modal_Document_Models_CVPR_2023_paper.pdf)]
[[Github](https://github.com/CyberAgentAILab/flex-dm)] <br>

**Unifying Layout Generation with a Decoupled Diffusion Model** <br>
*Mude Hui, Zhizheng Zhang, Xiaoyi Zhang, Wenxuan Xie, Yuwang Wang, Yan Lu.* <br>
CVPR 2023, Microsoft Research Asi & Xi’an Jiaotong University <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2303.05049)] <br>

**Layout Generation as Intermediate Action Sequence Prediction** <br>
*Huiting Yang, Danqing Huang, Chin-Yew Lin, Shengfeng He.* <br>
AAAI 2023, Microsoft Research Asia & South China University of Technology <br>
**Content-Agnostic** [[Paper](https://ojs.aaai.org/index.php/AAAI/article/download/26277/26049)]
[[Github](https://github.com/BERYLSHEEP/LayoutActionProject)] <br>

**Machine Learning Model to Evaluate the Appropriateness of Layout for Automatic Generation of Graphic Design Works** <br>
*Kohei Ishiyama, Taketoshi Ushiama.* <br>
IMCOM 2023, Kyushu University <br>
**Content-Agnostic** [[Paper](https://ieeexplore.ieee.org/abstract/document/10035646)] <br>

## 2022

**Geometry Aligned Variational Transformer for Image-conditioned Layout Generation** <br>
*Yunning Cao, Ye Ma, Min Zhou, Chuanbin Liu, Hongtao Xie, Tiezheng Ge, Yuning Jiang.* <br>
ACMMM 2022, Alibaba Group & University of Science and Technology of China <br>
**Content-Aware** [[Paper](https://arxiv.org/abs/2209.00852)] <br>

**BLT: Bidirectional Layout Transformer for Controllable Layout Generation**
*Xiang Kong, Lu Jiang, Huiwen Chang, Han Zhang, Yuan Hao, Haifeng Gong, Irfan Essa.* <br>
ECCV 2022, Google & Carnegie Mellon University<br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2112.05112v2)]
[[Github](https://github.com/google-research/google-research/tree/master/layout-blt)]
[[Project](https://shawnkx.github.io/blt)] <br>

**Composition-aware Graphic Layout GAN for Visual-textual Presentation Designs** <br>
*Min Zhou, Chenchen Xu, Ye Ma, Tiezheng Ge, Yuning Jiang, Weiwei Xu.* <br>
IJCAI 2022, Alibaba Group & Zhejiang University <br>
**Content-Aware** [[Paper](https://arxiv.org/abs/2205.00303)]
[[Project](https://tianchi.aliyun.com/dataset/142692)]
[[Github](https://github.com/minzhouGithub/CGL-GAN)]
[[Dataset](https://tianchi.aliyun.com/dataset/142692)] <br>

**Coarse-to-Fine Generative Modeling for Graphic Layouts** <br>
*Zhaoyun Jiang, Shizhao Sun, Jihua Zhu, Jian-Guang Lou, Dongmei Zhang.* <br>
AAAI 2022, Microsoft Research Asia & Xi’an Jiaotong University <br>
**Content-Agnostic** [[Paper](https://ojs.aaai.org/index.php/AAAI/article/download/19994/19753)]
[[Github](https://github.com/microsoft/LayoutGeneration)] <br>

**Aesthetics++: Refining graphic designs by exploring design principles and human preference** <br>
*Wenyuan Kong, Zhaoyun Jiang, Shizhao Sun, Zhuoning Guo, Weiwei Cui, Ting Liu, Jian-Guang Lou, and Dongmei Zhang.* <br>
TVCG 2022, Microsoft Research Asi & Peking University & Xi’an Jiaotong University <br>
**Content-Agnostic** [[Paper](https://ieeexplore.ieee.org/abstract/document/9714170/)]
[[Github](https://github.com/microsoft/LayoutGeneration)] <br>

## 2021

**Constrained Graphic Layout Generation via Latent Optimization** <br>
*Kotaro Kikuchi, Edgar Simo-Serra, Mayu Otani, Kota Yamaguchi.* <br>
ACMMM 2021, CyberAgent & Waseda University <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2108.00871)]
[[Github](https://github.com/ktrk115/const_layout)] <br>

**RUITE: Refining UI Layout Aesthetics Using Transformer Encoder** <br>
*Soliha Rahman, Vinoth Pandian Sermuga Pandian, Matthias Jarke.* <br>
IUI 2021, RWTH Aachen University <br>
[[Paper](https://dl.acm.org/doi/abs/10.1145/3397482.3450716)]
[[Github](https://github.com/vinothpandian/RUITE)] <br>

**LayoutTransformer: Layout Generation and Completion with Self-attention** <br>
*Kamal Gupta, Justin Lazarow, Alessandro Achille, Larry Davis, Vijay Mahadevan, Abhinav Shrivastava.* <br>
ICCV 2021, Amazon & University of Maryland <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2006.14615)]
[[Github](https://github.com/kampta/DeepLayout)] <br>

**CanvasVAE: Learning to Generate Vector Graphic Documents** <br>
*Kota Yamaguchi.* <br>
ICCV 2021, CyberAgent <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2108.01249)]
[[Github](https://github.com/CyberAgentAILab/canvas-vae)]
[[Dataset](https://github.com/CyberAgentAILab/canvas-vae/blob/main/docs/crello-dataset.md)] <br>

**LayoutTransformer: Scene Layout Generation with Conceptual and Spatial Diversity** <br>
*Cheng-Fu Yang, Wan-Cyuan Fan, Fu-En Yang, Yu-Chiang Frank Wang.* <br>
CVPR 2021, ASUS & National Taiwan University <br>
**Content-Agnostic** [[Paper](https://openaccess.thecvf.com/content/CVPR2021/papers/Yang_LayoutTransformer_Scene_Layout_Generation_With_Conceptual_and_Spatial_Diversity_CVPR_2021_paper.pdf)]
[[Github](https://github.com/davidhalladay/LayoutTransformer)] <br>

**Variational Transformer Networks for Layout Generation** <br>
*Diego Martin Arroyo, Janis Postels, Federico Tombari.* <br>
CVPR 2021, Google & ETH <br>
**Content-Agnostic** [[Paper](https://openaccess.thecvf.com/content/CVPR2021/papers/Arroyo_Variational_Transformer_Networks_for_Layout_Generation_CVPR_2021_paper.pdf)] <br>

**Attribute-conditioned Layout GAN for Automatic Graphic Design** <br>
*Jianan Li, Jimei Yang, Jianming Zhang, Chang Liu, Christina Wang, Tingfa Xu.* <br>
TVCG 2021, Adobe & Beijing Institute of Technology <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2009.05284)] <br>

## 2019-2020

**READ: Recursive Autoencoders for Document Layout Generation** <br>
*Akshay Gadi Patil, Omri Ben-Eliezer, Or Perel, Hadar Averbuch-Elor.* <br>
CVPRW 2020, Amazon & Simon Fraser University <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/1909.00302v4)] <br>

**Neural Design Network: Graphic Layout Generation with Constraints** <br>
*Hsin-Ying Lee, Lu Jiang, Irfan Essa, Phuong B Le, Haifeng Gong, Ming-Hsuan Yang, Weilong Yang.* <br>
ECCV 2020, Google Research & University of California, Merced <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/1912.09421v2)] <br>

**Retrieve-Then-Adapt: Example-based Automatic Generation for Proportion-related Infographics**
*Chunyao Qian, Shizhao Sun, Weiwei Cui, Jian-Guang Lou, Haidong Zhang, Dongmei Zhang.* <br>
VIS 2020, Microsoft Research Asia <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2008.01177)]
[[Github](https://github.com/microsoft/LayoutGeneration)] <br>

**Content-Aware Generative Modeling of Graphic Design Layouts** <br>
*Xinru Zheng, Xiaotian Qiao, Ying Cao, Rynson W.H. Lau.* <br>
ACM TOG 2019 / SIGGRAPH 2019, City University of Hong Kong <br>
**Content-Aware** [[Paper](https://xtqiao.com/projects/content_aware_layout/paper.pdf)]
[[Project](https://xtqiao.com/projects/content_aware_layout/)]
[[Code](https://portland-my.sharepoint.com/personal/xqiao6-c_my_cityu_edu_hk/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fxqiao6%2Dc%5Fmy%5Fcityu%5Fedu%5Fhk%2FDocuments%2FWork%2FProject%2FLayoutNet&ga=1)]
[[Dataset1](https://portland-my.sharepoint.com/personal/xqiao6-c_my_cityu_edu_hk/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fxqiao6%2Dc%5Fmy%5Fcityu%5Fedu%5Fhk%2FDocuments%2FWork%2FProject%2FDataset&ga=1)]
[[Dataset2](https://huggingface.co/datasets/creative-graphic-design/Magazine)]
[[Dataset3](https://github.com/creative-graphic-design/huggingface-datasets_Magazine)] <br>

**LayoutVAE: Stochastic Scene Layout Generation From a Label Set** <br>
*Akash Abdu Jyothi, Thibaut Durand, Jiawei He, Leonid Sigal, Greg Mori.* <br>
ICCV 2019, Borealis AI & Simon Fraser University & University of British Columbia <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/1907.10719)]
[[Github](https://github.com/Layout-Generation/layout-generation/tree/master/LayoutVAE)] <br>

**LayoutGAN: Generating Graphic Layouts with Wireframe Discriminators** <br>
*Jianan Li, Jimei Yang, Aaron Hertzmann, Jianming Zhang, Tingfa Xu.* <br>
ICLR 2019, Adobe & Beijing Institute of Technology <br>
TPAMI 2020 (LayoutGAN: Synthesizing Graphic Layouts with Vector-Wireframe Adversarial Networks) <br>
**Content-Agnostic** [[ICLR_Paper1](https://openreview.net/pdf?id=HJxB5sRcFQ)]
[[ICLR_Paper2](https://arxiv.org/abs/1901.06767)]
[[TPAMI_Paper](https://ieeexplore.ieee.org/abstract/document/8948239)]
[[Github-1](https://github.com/JiananLi2016/LayoutGAN-Tensorflow)]
[[Github-2](https://github.com/billzhonggz/LayoutGAN)]
[[Github-3](https://github.com/Layout-Generation/layout-generation/tree/master/LayoutGAN)] <br>

## Before

**Automatic Generation of Visual-Textual Presentation Layout** <br>
*Xuyong Yang, Tao Mei, Ying-Qing Xu, Yong Rui, Shipeng Li.* <br>
ACM ToMM 2016, Microsoft Research Asia & University of Science and Technology of China <br>
[[Paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/08/a33-yang.pdf)] <br>

**DesignScape: Design with Interactive Layout Suggestions** <br>
*Peter O’Donovan, Aseem Agarwala, Aaron Hertzmann.* <br>
CHI 2015, Adobe & the University of Toronto <br>
[[Paper](https://www.dgp.toronto.edu/~donovan/design/designscape.pdf)]
[[Project](https://www.dgp.toronto.edu/~donovan/design/)] <br>

**Learning Layouts for Single-Page Graphic Designs** <br>
*Peter O’Donovan, Aseem Agarwala, Aaron Hertzmann.* <br>
TVCG 2014, Adobe & the University of Toronto <br>
[[Paper](https://www.dgp.toronto.edu/~donovan/layout/designLayout.pdf)]
[[Project](https://www.dgp.toronto.edu/~donovan/layout/)] <br>

## Reference
https://github.com/JosephKJ/Awesome-Layout-Generators <br>
https://github.com/huapohen/Awesome-Layout-Generation <br>
https://github.com/Layout-Generation/layout-generation <br>
https://github.com/microsoft/LayoutGeneration <br>
https://github.com/jdily/awesome-layout-generation <br>
