from ultralytics import YOLO

# 加载预训练的模型
model = YOLO('./slime/slime_train/weights/best.pt')

model.predict('detects/slime/', project="slime",name="slime_predict",save=True,save_txt=True,save_conf=True, conf=0.15,exist_ok=True)
# model.predict('detects', project="slime",name="slime_predict",save=True,save_txt=True,save_conf=True, conf=0.5,exist_ok=True)
# model.predict('slime2.jpg', project="slime",save=True,save_txt=True,save_conf=True, imgsz=320, conf=0.5)