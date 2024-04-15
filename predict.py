from ultralytics import YOLO

image_path = ""

model = YOLO("withcovid.pt")

model(image_path)



