# Dilated Strip-Wise Spatial Feature Pyramid: An Efficient Network for Object Detection

**A Novel Approach to Enhanced Feature Representation for High-Performance Object Detection**

---

## 📋 Publication Information

**Presented at the 2025 IEEE 34th International Symposium on Industrial Electronics (ISIE)**  
**Publication Date:** June 20, 2025  
**DOI:** [10.1109/ISIE.2025.11124807](https://ieeexplore.ieee.org/abstract/document/11124807)

---

## 👥 Authors

| Name | Affiliation |
|------|-------------|
| **Harish Sundaralingam** | Lakehead University, Canada |
| **Tharrengini Suresh** | Lakehead University, Canada |
| **Thangarajah Akilan** | Lakehead University, Canada |
| **Saad Bin Ahmed** | Lakehead University, Canada |

**Corresponding Author:** Harish Sundaralingam (hsundara@lakeheadu.ca)

---

## 🔬 Abstract

This paper introduces **Dilated Strip-Wise Spatial Feature Pyramid (DSSFP)**, a novel neural network architecture designed to address the critical challenge of efficient feature representation in object detection systems. The proposed method employs an innovative **Atrous Split Depthwise Convolution (ASDC)** mechanism that strategically utilizes dilated depthwise strip convolution blocks with varying dilation rates (1, 3, and 6) to capture multi-scale contextual information while maintaining computational efficiency. Our approach significantly improves feature representation capabilities without substantially increasing model complexity, making it particularly suitable for resource-constrained deployment scenarios. Experimental results demonstrate that integrating DSSFP with existing detection frameworks yields substantial performance improvements across multiple benchmark datasets, establishing new state-of-the-art results on the VisDrone and AI-TOD object detection benchmarks.

---

## 🎯 Key Contributions

1. **Novel Feature Pyramid Architecture**: Introduces DSSFP, a dilated strip-wise spatial feature pyramid that enhances multi-scale feature representation for object detection.

2. **Efficient Convolution Design**: Proposes Atrous Split Depthwise Convolution (ASDC) that leverages dilated depthwise strip convolutions with multiple dilation rates to capture both local and global contextual information.

3. **Computational Efficiency**: Achieves superior detection performance with reduced parameter count and computational complexity compared to existing state-of-the-art methods.

4. **Comprehensive Evaluation**: Demonstrates consistent improvements across multiple challenging benchmarks, including VisDrone and AI-TOD datasets.

5. **Transferable Framework**: The proposed DSSFP module can be seamlessly integrated with various detection backbones, offering broad applicability.

---

## 📖 Introduction

Object detection remains one of the fundamental challenges in computer vision, with applications ranging from autonomous driving and surveillance to medical imaging and robotics. Modern object detection systems rely heavily on feature pyramid networks to capture objects at different scales. However, traditional approaches often struggle with the trade-off between feature representation quality and computational efficiency.

The **Dilated Strip-Wise Spatial Feature Pyramid** addresses these limitations by introducing a novel mechanism for multi-scale feature extraction that:

- **Captures Multi-Scale Context**: Utilizes multiple dilation rates to process features at different receptive field sizes simultaneously.
- **Maintains Spatial Integrity**: Preserves spatial resolution through strip-wise convolution operations that efficiently cover elongated regions.
- **Reduces Computational Overhead**: Employs depthwise separable convolutions to minimize parameter count and computational cost.
- **Enhances Feature Discrimination**: Improves feature discriminability through strategic information fusion across scales.

---

## 🏗️ Methodology

### Atrous Split Depthwise Convolution (ASDC)

The core innovation of DSSFP lies in the Atrous Split Depthwise Convolution module, which comprises three parallel branches with different dilation rates:

| Dilation Rate | Receptive Field | Purpose |
|---------------|-----------------|---------|
| **1** | Small | Capture fine-grained local features |
| **3** | Medium | Process intermediate-scale patterns |
| **6** | Large | Encode broad contextual information |

This multi-rate approach enables the network to simultaneously analyze objects at various scales, significantly improving detection accuracy for objects of diverse sizes.

### Feature Pyramid Construction

The DSSFP architecture constructs a hierarchical feature pyramid where:

1. **Input Features**: Multi-scale features from the backbone network
2. **ASDC Processing**: Each scale is processed through the ASDC module
3. **Feature Fusion**: Outputs from different dilation rates are fused
4. **Output Pyramid**: Enhanced multi-scale features for detection heads

---

## 🖼️ Model Architecture

The DSSFP architecture integrates seamlessly with existing detection frameworks:

```
┌─────────────────────────────────────────────────────────────┐
│                    DSSFP Architecture                       │
├─────────────────────────────────────────────────────────────┤
│  Backbone Features → ASDC Module → Feature Pyramid → Det.   │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              Atrous Split Depthwise Conv             │   │
│  ├─────────────┬─────────────┬─────────────┬────────────┤   │
│  │ Dilated     │ Dilated     │ Dilated     │ Feature    │   │
│  │ Rate 1      │ Rate 3      │ Rate 6      │ Fusion     │   │
│  └─────────────┴─────────────┴─────────────┴────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 Experimental Results

### Performance Comparison on VisDrone Test Set

The VisDrone dataset presents significant challenges due to its diverse object scales, densities, and challenging imaging conditions. Our method demonstrates remarkable improvements:

| Model | Input Size | Params (M) ↓ | GFLOPS ↓ | AP (%) ↑ | AP50 (%) ↑ |
|-------|------------|--------------|----------|----------|------------|
| **YOLO Detectors** | | | | | |
| YOLOv8-M | 640×640 | 25.9 | 78.9 | 24.6 | 40.7 |
| YOLOv8-L | 640×640 | 43.7 | 165 | 26.1 | 42.7 |
| YOLOv9-S | 640×640 | 17.2 | 26.7 | 22.9 | 38.3 |
| YOLOv9-M | 640×640 | 20.1 | 76.8 | 25.2 | 42.0 |
| **UAV Detectors** | | | | | |
| QueryDet | 2400×2400 | 33.9 | 212 | 28.3 | 48.1 |
| Cascade RCNN+ | 736×736 | - | - | 17.67 | 34.9 |
| **Transformer Detectors** | | | | | |
| DETR | 1333×750 | 60.0 | 187 | 24.1 | 40.1 |
| Deformable DETR | 1333×800 | 40.0 | 173 | 27.1 | 42.2 |
| Sparse DETR | 1333×800 | 40.9 | 121 | 27.3 | 42.5 |
| RT-DETR-R50 (SOTA) | 640×640 | 42.0 | 136 | 28.4 | 47.0 |
| **Our Methods** | | | | | |
| GFL-ResNet101 (Baseline) | 640×640 | 51.3 | 112 | 22.4 | 36.8 |
| GFL-HRNet+DSSFP | 640×640 | 33.0 | 114 | 26.3 | 41.7 |
| **TAL-HRNet+DSSFP** | **640×640** | **33.0** | **114** | **27.4** | **46.4** |

### Performance Comparison on AI-TOD Test Set

The AI-TOD dataset specifically targets tiny object detection, where our method shows exceptional performance:

| Model | AP50 (%) ↑ | AP (%) ↑ |
|-------|------------|----------|
| Cascade R-CNN | 30.8 | 13.8 |
| DetectoRS | 32.9 | 14.8 |
| FSANet | 41.4 | 15.2 |
| SP-YOLOv8s | 48.4 | 22.7 |
| MSFE-YOLO | 50.1 | 22.8 |
| SOD-YOLOv8n | 50.7 | 23.4 |
| FM-RTDETR | 56.3 | 26.9 |
| **TAL-HRNet+DSSFP** | **59.9** | **27.8** |

---

## 🚀 Key Findings

1. **State-of-the-Art Performance**: TAL-HRNet+DSSFP achieves **27.4% AP** on VisDrone and **27.8% AP** on AI-TOD, outperforming previous methods.

2. **Parameter Efficiency**: With only **33.0M parameters** and **114 GFLOPS**, our method maintains competitive computational complexity.

3. **Scale Invariance**: The ASDC mechanism effectively handles objects across various scales, particularly excelling at tiny object detection.

4. **Framework Compatibility**: DSSFP seamlessly integrates with different detection architectures (GFL, TAL, HRNet).

---

## 🛠️ Installation & Usage

### Prerequisites

- Python 3.8+
- PyTorch 1.8+
- CUDA 11.0+ (for GPU acceleration)

### Setup

```bash
# Clone the repository
git clone https://github.com/your-repo/hr_dssfp.git
cd hr_dssfp

# Install dependencies
pip install -r ultralytics_req.txt

# Activate environment (if using provided scripts)
source activate_ultralytics.sh
```

### Running Inference

```python
from model import DSSFPDetector

# Initialize detector
detector = DSSFPDetector(
    backbone='hrnet',
    num_classes=80,
    pretrained=True
)

# Perform detection
results = detector.detect(image_path)
```

---

## 📚 Citation

If you find this work useful in your research, please cite:

```bibtex
@inproceedings{sundaralingam2025dilated,
  title={Dilated Strip-Wise Spatial Feature Pyramid: An Efficient Network for Object Detection},
  author={Sundaralingam, Harish and Suresh, Tharrengini and Akilan, Thangarajah and Ahmed, Saad Bin},
  booktitle={2025 IEEE 34th International Symposium on Industrial Electronics (ISIE)},
  pages={1--6},
  year={2025},
  organization={IEEE}
}
```

---

## 🙏 Acknowledgments

We thank Lakehead University and Compute Canada for providing the computational resources and research environment that made this work possible. We also acknowledge the open-source community for the tools and frameworks that facilitated this research.

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 📧 Contact

For questions or inquiries about this research, please contact:

- **Harish Sundaralingam**: hsundara@lakeheadu.ca
- **Research Group**: Lakehead University Computer Vision Intelligence and Data Lab

---

**Keywords:** attention awareness, deep learning, feature pyramid, object detection, computer vision, dilated convolution, multi-scale feature learning

---

*Last Updated: June 2025*  
*© 2025 DSSFP Authors. All rights reserved.*

