import cv2
import cvzone
from ultralytics import YOLO
import numpy as np

model = YOLO("yolo11n-pose.pt")

cv2.startWindowThread()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, (640, 480))

    results = model(frame)
    annotated_frame = results[0].plot()

    cv2.imshow("Human pose", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
