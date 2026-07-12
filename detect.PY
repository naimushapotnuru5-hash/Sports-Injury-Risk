from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Open video
video = cv2.VideoCapture("../datasets/sports.mp4")
if not video.isOpened():
    print("video not found")
    exit()

while True:
    ret, frame = video.read()
    if not ret:
        break

    results = model(frame)

    annotated = results[0].plot()

    cv2.imshow("Sports Injury Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()