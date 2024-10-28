# Awesome Layout Generation

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/wd1511/Awesome-Layout-Generation) 

- [Dataset](#dataset)
- [2024](#2024)
- [2023](#2023)
- [2022](#2022)
- [2021](#2021)
- [2019-2020](#2019-2020)
- [Before](#Before)
- [Reference](#Reference)

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

## 2024

**Design Element Aware Poster Layout Generation** <br>
*Yinan Li, Jia Chen, Yin Bai, Jia Cheng, Jun Lei.* <vr>
CIKM 2024, Mtituan <br>
**Content-Aware** [[Paper](https://dl.acm.org/doi/abs/10.1145/3627673.3679557)] <br>

**Layout-Corrector: Alleviating Layout Sticking Phenomenon in Discrete Diffusion Model** <br>
*Shoma Iwai, Atsuki Osanai, Shunsuke Kitada, Shinichiro Omachi.* <br>
ECCV 2024, Tohoku University & LY Corporation <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2409.16689)] <br>

**GlyphDraw2: Automatic Generation of Complex Glyph Posters with Diffusion Models and Large Language Models** <br>
*Jian Ma, Yonglin Deng, Chen Chen, Haonan Lu, Zhenyu Yang.* <br>
arXiv 2024, OPPO AI Center & CUHK Shenzhen <br>
[[Paper](https://arxiv.org/abs/2407.02252)] [[Github](https://github.com/OPPO-Mente-Lab/GlyphDraw2)]<br>

**SciPostLayout: A Dataset for Layout Analysis and Layout Generation of Scientific Posters** <br>
*Shohei Tanaka, Hao Wang, Yoshitaka Ushiku.* <br>
BMVC 2024, OMRON SINIC X Corporation & Waseda University <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2407.19787)] [[Github](https://github.com/omron-sinicx/scipostlayout)] <br>

**Predicting Visual Attention in Graphic Design Documents** <br>
*Souradeep Chakraborty, Zijun Wei, Conor Kelton, Seoyoung Ahn, Aruna Balasubramanian, Gregory J. Zelinsky, Dimitris Samaras.* <br>
arXiv 2024, Stony Brook University <br>
[[Paper](https://arxiv.org/pdf/2407.02439)] <br>

**Glyph-ByT5-v2: A Strong Aesthetic Baseline for Accurate Multilingual Visual Text Rendering** <br>
*Zeyu Liu, Weicong Liang, Yiming Zhao, Bohan Chen, Lin Liang, Lijuan Wang, Ji Li, Yuhui Yuan.* <br>
arXiv 2024, Microsoft <br>
[[Paper](https://arxiv.org/abs/2406.10208)] [[Project](https://glyph-byt5-v2.github.io)] [[Github](https://github.com/AIGText/Glyph-ByT5)]<br>

**OpenCOLE: Towards Reproducible Automatic Graphic Design Generation** <br>
*Naoto Inoue, Kento Masui, Wataru Shimoda, Kota Yamaguchi.* <br>
CVPRW 2024, CyberAgent <br>
[[Paper](https://arxiv.org/abs/2406.08232)] [[Github](https://github.com/CyberAgentAILab/OpenCOLE)]<br>

**PosterLLaVa: Constructing a Unified Multi-modal Layout Generator with LLM** <br>
*Tao Yang, Yingmin Luo, Zhongang Qi, Yang Wu, Ying Shan, Chang Wen Chen.* <br>
arXiv 2024, Tencent PCG <br>
**Content-Aware** **LLM-based** [[Paper](https://arxiv.org/abs/2406.02884)] [[Project](https://huggingface.co/spaces/posterllava/PosterLLaVA)] [[Github](https://github.com/posterllava/PosterLLaVA)] <br>

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
**LLM-based** [[Paper](https://arxiv.org/abs/2404.00995)] [[Github-1](https://github.com/jaepoong/PosterLlama)] [[Github-2](https://anonymous.4open.science/r/PosterLlama/readme.md)]<br>

**Constrained Layout Generation with Factor Graphs** <br>
*Mohammed Haroon Dupty, Yanfei Dong, Sicong Leng, Guoji Fu, Yong Liang Goh, Wei Lu, Wee Sun Lee.* <br>
CVPR 2024, PayPal & National University of Singapore <br>
[[Paper](https://arxiv.org/abs/2404.00385)] <br>

**LayoutFlow: Flow Matching for Layout Generation** <br>
*Julian Jorge Andrade Guerreiro, Naoto Inoue, Kento Masui, Mayu Otani, Hideki Nakayama.* <br>
ECCV 2024, CyberAgent & The University of Tokyo <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2403.18187)] [[Project](https://julianguerreiro.github.io/layoutflow/)] [[Github](https://github.com/JulianGuerreiro/LayoutFlow)]<br>

**Glyph-ByT5: A Customized Text Encoder for Accurate Visual Text Rendering** <br>
*Zeyu Liu, Weicong Liang, Zhanhao Liang, Chong Luo, Ji Li, Gao Huang, Yuhui Yuan.* <br>
arXiv 2024, Microsoft Research Asia & Tsinghua University <br>
[[Paper](https://arxiv.org/abs/2403.09622)] [[Project](https://glyph-byt5.github.io)] [[Github](https://github.com/AIGText/Glyph-ByT5)]<br>

**Visual Layout Composer: Image-Vector Dual Diffusion Model for Design Layout Generation** <br>
*Mohammad Amin Shabani, Zhaowen Wang, Difan Liu, Nanxuan Zhao, Jimei Yang, Yasutaka Furukawa.* <br>
CVPR 2024, Adobe & Simon Fraser University <br>
**Content-Aware** [[Paper](https://aminshabani.github.io/visual_layout_composer/pdfs/visual_layout_composer.pdf)] [[Project](https://aminshabani.github.io/visual_layout_composer/)] <br>

**Desigen: A Pipeline for Controllable Design Template Generation** <br>
*Haohan Weng, Danqing Huang, Yu Qiao, Zheng Hu, Chin-Yew Lin, Tong Zhang, C. L. Philip Chen.* <br>
CVPR 2024, Microsoft Research Asia & South China University of Technology <br>
[[Paper](https://arxiv.org/abs/2403.09093)] [[Github](https://github.com/whaohan/desigen)] <br>

**Retrieval-Augmented Layout Transformer for Content-Aware Layout Generation** <br>
*Daichi Horita, Naoto Inoue, Kotaro Kikuchi, Kota Yamaguchi, Kiyoharu Aizawa.* <br>
CVPR 2024(oral), CyberAgent & The University of Tokyo <br>
**Content-Aware** [[Paper](https://arxiv.org/abs/2311.13602)] [[Project](https://udonda.github.io/RALF/)] [[Github](https://github.com/CyberAgentAILab/RALF)] <br>

**LayoutNUWA: Revealing the Hidden Layout Expertise of Large Language Models** <br>
*Zecheng Tang, Chenfei Wu, Juntao Li, Nan Duan.* <br>
ICLR 2024, Microsoft Research Asia & Soochow University <br>
**Content-Agnostic** [[Paper](https://openreview.net/pdf?id=qCUWVT0Ayy)] [[Github](https://github.com/ProjectNUWA/LayoutNUWA)] <br>

**Towards Aligned Layout Generation via Diffusion Model with Aesthetic Constraints** <br>
*Jian Chen, Ruiyi Zhang, Yufan Zhou, Rajiv Jain, Zhiqiang Xu, Ryan Rossi, Changyou Chen.* <br>
ICLR 2024, Adobe Research & MBZUAI & University at Buffalo <br>
**Content-Agnostic** [[Paper](https://openreview.net/pdf?id=kJ0qp9Xdsh)]
[[Github](https://github.com/puar-playground/lace)] <br>

**Spot the Error: Non-autoregressive Graphic Layout Generation with Wireframe Locator** <br>
*Jieru Lin, Danqing Huang, Tiejun Zhao, Dechen Zhan, Chin-Yew Lin.* <br>
AAAI 2024, Microsoft Research & Harbin Institute of Technology <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2401.16375)] [[Github](https://github.com/ffffatgoose/SpotError)] <br>

**Dolfin: Diffusion Layout Transformers without Autoencoder** <br>
*Yilin Wang, Zeyuan Chen, Liangjun Zhong, Zheng Ding, Zhizhou Sha, Zhuowen Tu.* <br>
ECCV 2024, Tsinghua University & University of California, San Diego <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2310.16305)] <br>

**LayoutDETR: Detection Transformer Is a Good Multimodal Layout Designer** <br>
*Ning Yu, Chia-Chih Chen, Zeyuan Chen, Rui Meng, Gang Wu, Paul Josel, Juan Carlos Niebles, Caiming Xiong, Ran Xu.* <br>
ECCV 2024, Salesforce Research <br>
**Content-Aware** [[Paper](https://arxiv.org/abs/2212.09877)] [[Github](https://github.com/salesforce/LayoutDETR)]<br>

## 2023

**COLE: A Hierarchical Generation Framework for Multi-Layered and Editable Graphic Design** <br>
*Peidong Jia, Chenxuan Li, Yuhui Yuan, Zeyu Liu, Yichao Shen, Bohan Chen, Xingru Chen, Yinglin Zheng, Dong Chen, Ji Li, Xiaodong Xie, Shanghang Zhang, Baining Guo.* <br>
arXiv 2023, Microsoft Research Asia & Peking University <br>
[[Paper](https://arxiv.org/abs/2311.16974)] <br>

**Relation-Aware Diffusion Model for Controllable Poster Layout Generation** <br>
*Fengheng Li, An Liu, Wei Feng, Honghe Zhu, Yaoyu Li, Zheng Zhang, Jingjing Lv, Xin Zhu, Junjie Shen, Zhangang Lin, Jingping Shao.* <br>
CIKM 2023, JD & Nankai University <br>
**Content-Aware** [[Paper](https://arxiv.org/abs/2306.09086)] [[Github](https://github.com/liuan0803/RADM?tab=readme-ov-file)] [[Dataset](https://github.com/liuan0803/RADM?tab=readme-ov-file)] <br>

**LayoutPrompter: Awaken the Design Ability of Large Language Models**
*Jiawei Lin, Jiaqi Guo, Shizhao Sun, Zijiang James Yang, Jian-Guang Lou, Dongmei Zhang.* <br>
NeurIPS 2023, Microsoft Research Asia & Shanghai Jiao Tong University <br>
**LLM-based** [[Paper](https://proceedings.neurips.cc/paper_files/paper/2023/file/88a129e44f25a571ae8b838057c46855-Paper-Conference.pdf)] [[Github](https://github.com/microsoft/LayoutGeneration)] <br>

**LayoutGPT: Compositional Visual Planning and Generation with Large Language Models** <br>
*Weixi Feng, Wanrong Zhu, Tsu-jui Fu, Varun Jampani, Arjun Akula, Xuehai He, Sugato Basu, Xin Eric Wang, William Yang Wang.* <br>
NeurIPS 2023, Google & UC Santa Barbara <br>
**LLM-based** [[Paper](https://arxiv.org/abs/2305.15393)] [[Project](https://layoutgpt.github.io)] [[Github](https://github.com/weixi-feng/LayoutGPT)] <br>

**DLT: Conditioned layout generation with Joint Discrete-Continuous Diffusion Layout Transformer** <br>
*Elad Levi, Eli Brosh, Mykola Mykhailych, Meir Perez.* <br>
ICCV 2023, Wix.com <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2303.03755)] [[Project](https://wix-incubator.github.io/DLT/)] [[Github](https://github.com/wix-incubator/DLT)] <br>

**LayoutDiffusion: Improving Graphic Layout Generation by Discrete Diffusion Probabilistic Models** <br>
*Junyi Zhang, Jiaqi Guo, Shizhao Sun, Jian-Guang Lou, Dongmei Zhang.* <br>
ICCV 2023, Microsoft Research Asia & Shanghai Jiao Tong University <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2303.11589)] [[Github](https://github.com/microsoft/LayoutGeneration)] <br>

**A Parse-Then-Place Approach for Generating Graphic Layouts from Textual Descriptions** <br>
*Jiawei Lin, Jiaqi Guo, Shizhao Sun, Weijiang Xu, Ting Liu.* <br>
ICCV 2023, Microsoft Research Asia & Shanghai Jiao Tong University <br>
**Content-Agnostic** [[Paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Lin_A_Parse-Then-Place_Approach_for_Generating_Graphic_Layouts_from_Textual_Descriptions_ICCV_2023_paper.pdf)] [[Github](https://github.com/microsoft/LayoutGeneration)] <br>

**Diffusion-based Document Layout Generation** <br>
*Liu He, Yijuan Lu, John Corring, Dinei Florencio, Cha Zhang.* <br>
ICDAR 2023, Microsoft Cloud and AI & Purdue University <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2303.10787)] <br>

**PLay: Parametrically Conditioned Layout Generation using Latent Diffusion**
*Chin-Yi Cheng, Forrest Huang, Gang Li, Yang Li.* <br>
ICML 2023, Google Research <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2301.11529v2)] <br>

**PosterLayout: A New Benchmark and Approach for Content-aware Visual-Textual Presentation Layout** <br>
*HsiaoYuan Hsu, Xiangteng He, Yuxin Peng, Hao Kong, Qing Zhang.* <br>
CVPR 2023, Meituan & Peking University <br>
**Content-Aware** [[Paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Hsu_PosterLayout_A_New_Benchmark_and_Approach_for_Content-Aware_Visual-Textual_Presentation_CVPR_2023_paper.pdf)] [[Project](http://39.108.48.32/mipl/PosterLayout/)] [[Github](https://github.com/PKU-ICST-MIPL/PosterLayout-CVPR2023)] [[Dataset1](http://39.108.48.32/mipl/PosterLayout/)] [[Dataset2](https://huggingface.co/datasets/creative-graphic-design/PKU-PosterLayout)] <br>

**LayoutDM: Transformer-based diffusion model for layout generation** <br>
*Shang Chai, Liansheng Zhuang, Fengying Yan.* <br>
CVPR 2023, University of Science and Technology of China & Tianjin University <br>
**Content-Agnostic** [[Paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Chai_LayoutDM_Transformer-Based_Diffusion_Model_for_Layout_Generation_CVPR_2023_paper.pdf)] <br>

**LayoutDM: Discrete Diffusion Model for Controllable Layout Generation** <br>
*Naoto Inoue, Kotaro Kikuchi, Edgar Simo-Serra, Mayu Otani, Kota Yamaguchi.* <br>
CVPR 2023, CyberAgent & Waseda University <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2303.08137)] [[Project](https://cyberagentailab.github.io/layout-dm)] [[Github](https://github.com/CyberAgentAILab/layout-dm)] <br>

**LayoutFormer++: Conditional Graphic Layout Generation via Constraint Serialization and Decoding Space Restriction** <br>
*Zhaoyun Jiang, Jiaqi Guo, Shizhao Sun, Huayu Deng, Zhongkai Wu, Vuksan Mijovic, Zijiang James Yang, Jian-Guang Lou, Dongmei Zhang.* <br>
CVPR 2023, Microsoft Research Asi & Xi’an Jiaotong University <br>
**Content-Agnostic** [[Paper](http://arxiv.org/abs/2208.08037)] [[Github](https://github.com/microsoft/LayoutGeneration)] <br>

**Towards Flexible Multi-modal Document Models** <br>
*Naoto Inoue, Kotaro Kikuchi, Edgar Simo-Serra, Mayu Otani, Kota Yamaguchi.* <br>
CVPR 2023, CyberAgent & Waseda University <br>
**Content-Agnostic** [[Paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Inoue_Towards_Flexible_Multi-Modal_Document_Models_CVPR_2023_paper.pdf)] [[Github](https://github.com/CyberAgentAILab/flex-dm)] <br>

**Unifying Layout Generation with a Decoupled Diffusion Model** <br>
*Mude Hui, Zhizheng Zhang, Xiaoyi Zhang, Wenxuan Xie, Yuwang Wang, Yan Lu.* <br>
CVPR 2023, Microsoft Research Asi & Xi’an Jiaotong University <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2303.05049)] <br>

**Layout Generation as Intermediate Action Sequence Prediction** <br>
*Huiting Yang, Danqing Huang, Chin-Yew Lin, Shengfeng He.* <br>
AAAI 2023, Microsoft Research Asia & South China University of Technology <br>
**Content-Agnostic** [[Paper](https://ojs.aaai.org/index.php/AAAI/article/download/26277/26049)] [[Github](https://github.com/BERYLSHEEP/LayoutActionProject)] <br>

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
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2112.05112v2)] [[Github](https://github.com/google-research/google-research/tree/master/layout-blt)] <br>

**Composition-aware Graphic Layout GAN for Visual-textual Presentation Designs** <br>
*Min Zhou, Chenchen Xu, Ye Ma, Tiezheng Ge, Yuning Jiang, Weiwei Xu.* <br>
IJCAI 2022, Alibaba Group & Zhejiang University <br>
**Content-Aware** [[Paper](https://arxiv.org/abs/2205.00303)] [[Project](https://tianchi.aliyun.com/dataset/142692)] [[Github](https://github.com/minzhouGithub/CGL-GAN)] [[Dataset](https://tianchi.aliyun.com/dataset/142692)] <br>

**Coarse-to-Fine Generative Modeling for Graphic Layouts** <br>
*Zhaoyun Jiang, Shizhao Sun, Jihua Zhu, Jian-Guang Lou, Dongmei Zhang.* <br>
AAAI 2022, Microsoft Research Asia & Xi’an Jiaotong University <br>
**Content-Agnostic** [[Paper](https://ojs.aaai.org/index.php/AAAI/article/download/19994/19753)] [[Github](https://github.com/microsoft/LayoutGeneration)] <br>

**Aesthetics++: Refining graphic designs by exploring design principles and human preference** <br>
*Wenyuan Kong, Zhaoyun Jiang, Shizhao Sun, Zhuoning Guo, Weiwei Cui, Ting Liu, Jian-Guang Lou, and Dongmei Zhang.* <br>
TVCG 2022, Microsoft Research Asi & Peking University & Xi’an Jiaotong University <br>
**Content-Agnostic** [[Paper](https://ieeexplore.ieee.org/abstract/document/9714170/)] [[Github](https://github.com/microsoft/LayoutGeneration)]

## 2021

**Constrained Graphic Layout Generation via Latent Optimization** <br>
*Kotaro Kikuchi, Edgar Simo-Serra, Mayu Otani, Kota Yamaguchi.* <br>
ACMMM 2021, CyberAgent & Waseda University <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2108.00871)] [[Github](https://github.com/ktrk115/const_layout)] <br>

**RUITE: Refining UI Layout Aesthetics Using Transformer Encoder** <br>
*Soliha Rahman, Vinoth Pandian Sermuga Pandian, Matthias Jarke.* <br>
IUI 2021, RWTH Aachen University <br>
[[Paper](https://dl.acm.org/doi/abs/10.1145/3397482.3450716)] [[Github](https://github.com/vinothpandian/RUITE)]

**LayoutTransformer: Layout Generation and Completion with Self-attention** <br>
*Kamal Gupta, Justin Lazarow, Alessandro Achille, Larry Davis, Vijay Mahadevan, Abhinav Shrivastava.* <br>
ICCV 2021, Amazon & University of Maryland <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2006.14615)] [[Github](https://github.com/kampta/DeepLayout)] <br>

**CanvasVAE: Learning to Generate Vector Graphic Documents** <br>
*Kota Yamaguchi.* <br>
ICCV 2021, CyberAgent <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2108.01249)] [[Github](https://github.com/CyberAgentAILab/canvas-vae)] [[Dataset](https://github.com/CyberAgentAILab/canvas-vae/blob/main/docs/crello-dataset.md)] <br>

**LayoutTransformer: Scene Layout Generation with Conceptual and Spatial Diversity** <br>
*Cheng-Fu Yang, Wan-Cyuan Fan, Fu-En Yang, Yu-Chiang Frank Wang.* <br>
CVPR 2021, ASUS & National Taiwan University <br>
**Content-Agnostic** [[Paper](https://openaccess.thecvf.com/content/CVPR2021/papers/Yang_LayoutTransformer_Scene_Layout_Generation_With_Conceptual_and_Spatial_Diversity_CVPR_2021_paper.pdf)] [[Github](https://github.com/davidhalladay/LayoutTransformer)] <br>

**Variational Transformer Networks for Layout Generation** <br>
*Diego Martin Arroyo, Janis Postels, Federico Tombari.* <br>
CVPR 2021, Google & ETH <br>
**Content-Agnostic** [[Paper](https://openaccess.thecvf.com/content/CVPR2021/papers/Arroyo_Variational_Transformer_Networks_for_Layout_Generation_CVPR_2021_paper.pdf)] <br>

**Attribute-Conditioned Layout GAN for Automatic Graphic Design** <br>
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
**Content-Agnostic** [[Paper](https://arxiv.org/abs/2008.01177)] [[Github](https://github.com/microsoft/LayoutGeneration)] <br>

**Content-Aware Generative Modeling of Graphic Design Layouts** <br>
*Xinru Zheng, Xiaotian Qiao, Ying Cao, Rynson W.H. Lau.* <br>
ACM TOG 2019 / SIGGRAPH 2019, City University of Hong Kong <br>
**Content-Aware** [[Paper](https://xtqiao.com/projects/content_aware_layout/paper.pdf)] [[Project](https://xtqiao.com/projects/content_aware_layout/)] [[Code](https://portland-my.sharepoint.com/personal/xqiao6-c_my_cityu_edu_hk/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fxqiao6%2Dc%5Fmy%5Fcityu%5Fedu%5Fhk%2FDocuments%2FWork%2FProject%2FLayoutNet&ga=1)] [[Dataset1](https://portland-my.sharepoint.com/personal/xqiao6-c_my_cityu_edu_hk/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fxqiao6%2Dc%5Fmy%5Fcityu%5Fedu%5Fhk%2FDocuments%2FWork%2FProject%2FDataset&ga=1)] [[Dataset2](https://huggingface.co/datasets/creative-graphic-design/Magazine)] [[Dataset3](https://github.com/creative-graphic-design/huggingface-datasets_Magazine)] <br>

**LayoutVAE: Stochastic Scene Layout Generation From a Label Set** <br>
*Akash Abdu Jyothi, Thibaut Durand, Jiawei He, Leonid Sigal, Greg Mori.* <br>
ICCV 2019, Borealis AI & Simon Fraser University & University of British Columbia <br>
**Content-Agnostic** [[Paper](https://arxiv.org/abs/1907.10719)] [[Github](https://github.com/Layout-Generation/layout-generation/tree/master/LayoutVAE)] <br>

**LayoutGAN: Generating Graphic Layouts with Wireframe Discriminators** <br>
*Jianan Li, Jimei Yang, Aaron Hertzmann, Jianming Zhang, Tingfa Xu.* <br>
ICLR 2019, Adobe & Beijing Institute of Technology <br>
TPAMI 2020 (LayoutGAN: Synthesizing Graphic Layouts with Vector-Wireframe Adversarial Networks) <br>
**Content-Agnostic** [[ICLR_Paper1](https://openreview.net/pdf?id=HJxB5sRcFQ)] [[ICLR_Paper2](https://arxiv.org/abs/1901.06767)] [[TPAMI_Paper](https://ieeexplore.ieee.org/abstract/document/8948239)] [[Github-1](https://github.com/JiananLi2016/LayoutGAN-Tensorflow)] [[Github-2](https://github.com/billzhonggz/LayoutGAN)] [[Github-3](https://github.com/Layout-Generation/layout-generation/tree/master/LayoutGAN)] <br>

## Before

**Automatic Generation of Visual-Textual Presentation Layout** <br>
*Xuyong Yang, Tao Mei, Ying-Qing Xu, Yong Rui, Shipeng Li.* <br>
ACM TOMM 2016, Microsoft Research Asia & University of Science and Technology of China <br>
[[Paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/08/a33-yang.pdf)] <br>

**DesignScape: Design with Interactive Layout Suggestions** <br>
*Peter O’Donovan, Aseem Agarwala, Aaron Hertzmann.* <br>
CHI 2015, Adobe & the University of Toronto <br>
[[Paper](https://www.dgp.toronto.edu/~donovan/design/designscape.pdf)] [[Project](https://www.dgp.toronto.edu/~donovan/design/)] <br>

**Learning Layouts for Single-Page Graphic Designs** <br>
*Peter O’Donovan, Aseem Agarwala, Aaron Hertzmann.* <br>
TVCG 2014, Adobe & the University of Toronto <br>
[[Paper](https://www.dgp.toronto.edu/~donovan/layout/designLayout.pdf)] [[Project](https://www.dgp.toronto.edu/~donovan/layout/)] <br>

## Reference
https://github.com/huapohen/Awesome-Layout-Generation <br>
https://github.com/Layout-Generation/layout-generation <br>
https://github.com/microsoft/LayoutGeneration <br>
https://github.com/jdily/awesome-layout-generation <br>
https://github.com/JosephKJ/Awesome-Layout-Generators <br>
