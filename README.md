1. Requirements:
    - Python 3.7
    - requirements.txt

2. Install:
    - Install ultralytics - ```pip install ultralytics```
    - Install deepSORT - ```cd deep_sort_realtime``` && ```pip3 install .```
    - Install opencv - ```pip install opencv-python```
    - Install cvzone - ```pip install cvzone```

3. Run code:
    - download weights - ```https://drive.google.com/drive/folders/1-TsoCiUbgqIDsvVTJmLeAxoI6uXyvQkZ?usp=sharing``` and add their in project folder (recommended to use "yolov8n.pt" )
    - indicate your weights in "model" (line 16)
    - indicate video link in "capture = " (line 101)