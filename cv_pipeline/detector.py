from ultralytics import YOLO
import cv2

class ObjectDetector:

    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect(self, image_path):
        results = self.model(image_path)
        detections = []

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                label = self.model.names[cls_id]

                detections.append(label)

        return detections
