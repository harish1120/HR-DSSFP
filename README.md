# DSSFP

This is the official implementation of the paper:
  * [Dilated Strip-Wise Spatial Feature Pyramid: An Efficient Network for Object Detection](https://ieeexplore.ieee.org/abstract/document/11124807)
    
**Model Architecture**
---
![Model Arch](dssfp.svg)

**Atrous Split Depthwise Conv that utilizes Dilated Depthwise Strip Conv blocks
with dilation rates 1, 3, and 6 for better feature representation.**
---
![Training](ASDC.svg)

**Experimental Results**
---
### Overall comparison of the Proposed Model on the VisDrone Test Set

| **Model**                     | **Input Size** | **Params (M) ↓** | **GFLOPS ↓** | **AP (%) ↑** | **AP50 (%) ↑** |
|-------------------------------|----------------|------------------|--------------|--------------|----------------|
| **YOLO Detectors**            |                |                  |              |              |                |
| YOLOv8-M                      | 640×640        | 25.9             | 78.9         | 24.6         | 40.7           |
| YOLOv8-L                      | 640×640        | 43.7             | 165          | 26.1         | 42.7           |
| YOLOv9-S                      | 640×640        | 17.2             | 26.7         | 22.9         | 38.3           |
| YOLOv9-M                      | 640×640        | 20.1             | 76.8         | 25.2         | 42.0           |
| **UAV Detectors**             |                |                  |              |              |                |
| QueryDet                      | 2400×2400      | 33.9             | 212          | 28.3         | 48.1           |
| Cascade RCNN+                 | 736×736        | -                | -            | 17.67        | 34.9           |
| **Transformer Detectors**     |                |                  |              |              |                |
| DETR                          | 1333×750       | 60.0             | 187          | 24.1         | 40.1           |
| Deformable DETR               | 1333×800       | 40.0             | 173          | 27.1         | 42.2           |
| Sparse DETR                   | 1333×800       | 40.9             | 121          | 27.3         | 42.5           |
| RT-DETR-R50 (SOTA)            | 640×640        | 42.0             | 136          | 28.4         | 47.0           |
| **Our Methods**               |                |                  |              |              |                |
| GFL-ResNet101 (Baseline)      | 640×640        | 51.3             | 112          | 22.4         | 36.8           |
| GFL-HRNet+DSSFP               | 640×640        | 33.0             | 114          | 26.3         | 41.7           |
| **TAL-HRNet+DSSFP**           | **640×640**    | **33.0**         | **114**      | **27.4**     | **46.4**       |

### Overall comparison of the Proposed Model on the AI-TOD Test Set

| Model                 | AP50 (%) ↑ | AP (%) ↑ |
|-----------------------|------------|----------|
| Cascade R-CNN         | 30.8       | 13.8     |
| DetectoRS             | 32.9       | 14.8     |
| FSANet                | 41.4       | 15.2     |
| SP-YOLOv8s            | 48.4       | 22.7     |
| MSFE-YOLO             | 50.1       | 22.8     |
| SOD-YOLOv8n           | 50.7       | 23.4     |
| FM-RTDETR             | 56.3       | 26.9     |
| **TAL-HRNet-DSSFP**   | **59.9**   | **27.8** |


*Note: ↓ (Lower is better), ↑ (Higher is better).*
-->
