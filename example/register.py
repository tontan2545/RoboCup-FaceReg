import cv2
from RoboCup.ra_face_recognition import RAFaceRecognition
if(__name__ == "__main__"):
    raFaceRecognition = RAFaceRecognition("../database")
    vid = cv2.VideoCapture(0)

    while(True):
        rect, frame = vid.read()
        cv2.imshow("video", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()