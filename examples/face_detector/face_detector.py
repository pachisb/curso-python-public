#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# From: https://towardsdatascience.com/face-detection-in-10-lines-for-beginners-1787aa1d9127


# OpenCV
import cv2

HAAR_FILE_PATH = "examples/face_detector/haarcascade_frontalface_default.xml"
WEBCAM_ID = 0  # NOTE: try 1 or 2 if several cameras are available
IMAGE_PATH = "img/students.jpg"

def face_video():
    face_cascade = cv2.CascadeClassifier(HAAR_FILE_PATH)
    video = cv2.VideoCapture(WEBCAM_ID)
    while True:
        ret, image = video.read()
        if not ret:
            continue
        image = cv2.flip(image, 1)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray_image, scaleFactor=1.05, minNeighbors=5)
        for(x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 1)
        cv2.imshow('Face Detector', image)

        k = cv2.waitKey(10)
        if k == ord('q') or k == ord('Q'):
            break

    video.release()
    cv2.destroyAllWindows()


def face_image():
    face_cascade = cv2.CascadeClassifier(HAAR_FILE_PATH)
    image = cv2.imread(IMAGE_PATH)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_image,
                                          scaleFactor=1.05,
                                          minNeighbors=5)  # "Precision"
    print(f"{len(faces)} faces detected in the image")

    for x, y, w, h in faces:
        image = cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 1)
        cv2.imshow("Face Detector", image)
        #cv2.imwrite("output.jpg", image)

    while(True):
        k = cv2.waitKey(50)
        if k == ord('q') or k == ord('Q'):
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    print("NOTE: press q to stop each of the two parts!")
    face_video()
    face_image()
