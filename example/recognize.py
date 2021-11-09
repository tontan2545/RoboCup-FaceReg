import cv2
import time
from RoboCup.ra_face_recognition import RAFaceRecognition

font = cv2.FONT_HERSHEY_DUPLEX

if __name__ == "__main__":
    raFaceRecognition = RAFaceRecognition("../database")
    vid = cv2.VideoCapture(0)
    while (True):
        rect, frame = vid.read()
        currentTime = time.process_time()
        names = raFaceRecognition.detectFace(frame)

        for name in names:
            top, right, bottom, left = names[name]
            cv2.rectangle(frame, (left,top), (right,bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (left, bottom+30), font, 1.0, (0, 0, 255), 2)

        cv2.putText(frame, "FPS: " + str(round(1/(time.process_time() - currentTime))), (10,80), font, 1.0, (0, 0, 255), 2)

        cv2.imshow("recognize", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()
