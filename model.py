import os
from ultralytics import YOLO
from torchinfo import summary

model = YOLO("ultralytics/ultralytics/cfg/mymodels/dssfp.yaml", verbose=True)

input_size = (1, 3, 640, 640)
summary(
        model.model,
        input_size=input_size,
        col_names=("kernel_size", "output_size", "num_params", "trainable"),
        depth=3,                # how many levels of nested modules to show
        device='cpu',   
        verbose=1               # 0=no model info, 1=layer info, 2=param info
    )


train_results = model.train(
    data="/ultralytics/ultralytics/cfg/datasets/ai-tod.yaml",  # Path to dataset configuration file
    epochs=300,  # Number of training epochs
    imgsz=640,
    batch=0.30,
    device='cpu',
    patience=10,
    save_period=5,
    cache='disk',
    amp=True,
    val=True,
    save_json=True, 
    pretrained=True, 
    plots=True,
    resume=True,
    mixup=0.5,
    degrees=10,
    deterministic=False,
    workers=4
    )



# Evaluate the model's performance on the validation set
metrics = model.val(split='val',save_json=True,plots=True,name='val')
print("\nVal Metrics:")
print(f"mAP50-95: {metrics.box.map:.5f}")
print(f"mAP50: {metrics.box.map50:.5f}")

test_results = model.val(
    data="/home/harishs/projects/def-akilan/harishs/detection/ultralytics/ultralytics/cfg/datasets/ai-tod.yaml",
    split='test',
    imgsz=640,
    conf=0.001,
    iou=0.65,
    name='test',
    save_json=True,
    save_conf=True,
    save_txt=True,
    plots=True
)

# 4. Analyze results
print("\nTest Metrics:")
print(f"mAP50-95: {test_results.box.map:.5f}")
print(f"mAP50: {test_results.box.map50:.5f}")
