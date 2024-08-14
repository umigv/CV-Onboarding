from ultralytics import YOLO

model = YOLO("your_model_name.pt")

model.predict(source = "chosen_competition_video.mp4", show=True, save=True, hide_labels=True, conf=0.5, save_txt=False, save_crop=False, line_thickness=2)
