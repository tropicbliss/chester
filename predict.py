from ultralytics import YOLO

file_path = ""

model = YOLO("withcovid.pt")

model(file_path)



