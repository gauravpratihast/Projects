import cv2
import numpy as np
import dlib
from sklearn.neighbors import KNeighborsClassifier
import keyboard

import os

data = np.load("face_expression.npy")
print(data.shape)

X = data[:, 1:].astype(int)
y = data[:, 0]

model = KNeighborsClassifier()
model.fit(X, y)

detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

cap = cv2.VideoCapture(0)


while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        landmarks = predictor(gray, face)

        expression = np.array([[point.x - face.left(), point.y - face.top()] for point in landmarks.parts()[17:]])
        prediction = model.predict([expression.flatten()])
        print(prediction)


        # print(f'looking {prediction[0]}')
        # lip_up = landmarks.parts()[62].y
        # lip_down = landmarks.parts()[66].y
        # #
        # if lip_down - lip_up > 5:
        #     keyboard.press('up')
        # else:
        #     keyboard.press('down')


    if ret:
        cv2.imshow('My window', frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()