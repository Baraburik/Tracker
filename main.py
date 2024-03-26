from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

tracker = DeepSort(max_age=5)

video_path = 'rtsp://admin:QWEqwe123@192.168.1.64:554/ISAPI/Streaming/Channels/101' #
model = YOLO('yolov8n.pt')  # put your weights
results = model(video_path, show=True)

for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs

    bbs = result.detect(video_path)
    tracks = tracker.update_tracks(bbs, frame=video_path)
    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        ltrb = track.to_ltrb()
