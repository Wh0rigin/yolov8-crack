from ultralytics import YOLO
 
# 加载模型
# model = YOLO("yolov8n.yaml")  # 从头开始构建新模型
model = YOLO("yolov8n.pt")  # 加载预训练模型（推荐用于训练）
 
# Use the model
# results = model.train(data="ultralytics/datasets/rain.yaml", epochs=20, batch=-1)  # 训练模型
if __name__ == '__main__':
    # Use the model
    results = model.train(project="slime",name="slime_train",data="datasets/genshin/slime/slime.yaml",
                          exist_ok=True, epochs=100, batch=-1,save_period=10,save=True,verbose=True)  # 训练模型
    results = model.val()  
    # results = model("img.jpg")
    # success = YOLO("yolov8n.pt").export(format="onnx") 