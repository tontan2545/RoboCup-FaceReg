import cv2
import os
import face_recognition
import pickle
from RoboCup.ra_face_recognition import RAFaceRecognition

if(__name__ == "__main__"):
    raFaceRecognition = RAFaceRecognition("../database")
    vid = cv2.VideoCapture(0)

    while(True):
        rect, frame = vid.read()
        width = vid.get(3)
        height = vid.get(4)

        plain_frame = frame.copy()

        cv2.rectangle(frame, (int(width/3) , int(height/6)), (int(width*2/3), int(height*5/6)), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, "Press 's' to register", (int(width/3), int(height*5/6) + 30), font, 1.0, (0, 0, 255), 2)

        cv2.imshow("video", frame)

        pressedKey = cv2.waitKey(1) & 0xFF
        if pressedKey == ord('q'):
            break
        elif pressedKey == ord('s'):
            name = input("Enter name: ")
            status = raFaceRecognition.register(name, plain_frame)
            print(status["message"])
            break
    vid.release()
    cv2.destroyAllWindows()