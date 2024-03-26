from ultralytics import YOLO

model = YOLO("yolov8n.yaml")  # build a new model from scratch


# Use the model
results = model.train(data = "config.yaml",epochs = 20)  # predict on an image


