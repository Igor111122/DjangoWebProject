"""
Definition of models.
"""

from django.db import models
from threading import *
import cv2
import time

def cam():
    while(1):
        # �������� ������ ������
        cap = cv2.VideoCapture(0)

        # "����������" ������, ����� ������ �� ��� �����
        for i in range(30):
            cap.read()

        # ������ ������    
        ret, frame = cap.read()

        # ���������� � ����
        cv2.imwrite('app/static/app/images/Cam.png', frame)   

        # ��������� ������
        cap.release()

t1 = Thread(target = cam)

t1.start()

# Create your models here.
