from ultralytics import YOLO

model = YOLO("Machine_Learning/best.pt")

model.predict(source = "Machine_Learning/f22_parking_lot_3.mp4", show=True, save=True, hide_labels=True, conf=0.5, save_txt=False, save_crop=False, line_thickness=2)
