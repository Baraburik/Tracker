import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

tracker = DeepSort(max_age=5)

video_path = 'rtsp://admin:QWEqwe123@192.168.1.64:554/ISAPI/Streaming/Channels/101'
model = YOLO('yolov8n.pt')  # put your weights

cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    success, frame = cap.read()

    if success:
        results = model.track(frame, persist=True)

        annotated_frame = results[0].plot()

        cv2.imshow("Frame", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
