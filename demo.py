import cv2
import torch
import torchvision

cap=cv2.VideoCapture(0)

while True:
    _, frame =cap.read()
