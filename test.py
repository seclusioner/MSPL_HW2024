import cv2
import math
import numpy as np
import os
import torch
import cvzone

from ultralytics import YOLO
# from sort import *

# %% Part1 Running yolo
'''
Test the yolo model on image 

output: class name、confidence value、bounding box

'''

model = YOLO('Yolo-Weights/yolov8l.pt') # create model
result = model('Images/1.jpg', show=True)
cv2.waitKey(0)

result = model('Images/2.jpg', show=True)
cv2.waitKey(0)

result = model('Images/3.jpg', show=True)
cv2.waitKey(0)

# %% Part2 Yolo with webcam
'''
Use yolo model on your webcam

'''
cap = cv2.VideoCapture(0) # ID number of webcam (0 or 1)
cap.set(3, 640)
cap.set(4, 480)

model = YOLO('Yolo-Weights/yolov8n.pt') # create model

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

while True:
    success, img = cap.read()
    results = model(img, stream=True)
    
    # check bounding box
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # opencv ==================
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0] # box.xywh[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # get the real values to used in opencv
            
            w, h = x2-x1, y2-y1
            
            # cvzone ==================
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 4)
            cvzone.cornerRect(img, (x1, y1, w, h))

            # Confidence value
            conf = math.ceil(box.conf[0]*100) / 100
            
            # Class name
            className = int(box.cls[0]) # get class id
            
            cvzone.putTextRect(img, f'{classNames[className]} {conf}', (max(0, x1), max(30, y1-20))) # to set the boundary for display box


            
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    