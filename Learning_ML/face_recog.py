import cv2
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

data = np.load("face_data.npy")

# print(data.shape, data.dtype)
print(data.shape)
# print(data[: 5])
X = data[:, 1:].astype(int)
y = data[:, 0]

model = KNeighborsClassifier()
model.fit(X, y)

cap = cv2.VideoCapture(0)

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:

    ret, frame = cap.read()

    if ret:
        faces = detector.detectMultiScale(frame)

        for face in faces:
            x, y, w, h = face
            # print(x, y, w, h)
            cut = frame[y:y+h, x:x+w]

            fix = cv2.resize(cut, (100, 100))
            gray = cv2.cvtColor(fix, cv2.COLOR_BGR2GRAY)

            out = model.predict([gray.flatten()])

            cv2.rectangle(frame, (x, y), (x+w, y+h), (100, 100, 100), 2)
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            cv2.rectangle(frame, (x, y+h), (x+h, y+h+25), (100, 100, 100), cv2.FILLED)



            # cv2.putText(frame, str(out[0]), (x + 1, y), cv2.FONT_ITALIC, 2, (231, 111, 120), 2)
            cv2.putText(frame, str(out[0]), (x, y+h+22), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 2)


            # print(out)

            # cv2.imshow("My Face", gray)

        cv2.imshow("My Screen", frame)


    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()