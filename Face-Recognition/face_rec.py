import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from PIL import ImageGrab
from os import times
import time

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
class FaceRecognition:
    def __init__(self):
        self.face=False
        self.path = "D:\\Files\College\\Sem V\\Programming Laboratry - II\\Project\\Face-Recognition\\Training_images\\"
        self.images = []
        self.classNames = []
        face=False
        self.myList = os.listdir(self.path)
        print(self.myList)
        for cl in self.myList:
            self.curImg = cv2.imread(f'{self.path}/{cl}')
            self.images.append(self.curImg)
            self.classNames.append(os.path.splitext(cl)[0])
        print(self.classNames)
        self.encodeListKnown=self.findEncodings(self.images)
        print('Encoding complete')
        self.recogniseFace()
    def recogniseFace(self):
        while True:
            cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
            success, img = cap.read()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(self.encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(self.encodeListKnown, encodeFace)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = self.classNames[matchIndex].upper()
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    print('Matched')
                    self.face=True  
                    time.sleep(5)          
                    break
                    
            if(self.face):
                cv2.destroyAllWindows()
                break
            else:
                cv2.imshow('Webcam', img)
                cv2.waitKey(1)
    def findEncodings(self,images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList
    