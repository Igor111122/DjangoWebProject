"""
Definition of models.
"""

from django.db import models
from threading import *
import cv2
import time

def cam():
    while(1):
        # Включаем первую камеру
        cap = cv2.VideoCapture(0)

        # "Прогреваем" камеру, чтобы снимок не был тёмным
        for i in range(30):
            cap.read()

        # Делаем снимок    
        ret, frame = cap.read()

        # Записываем в файл
        cv2.imwrite('app/static/app/images/Cam.png', frame)   

        # Отключаем камеру
        cap.release()

t1 = Thread(target = cam)

t1.start()

# Create your models here.
