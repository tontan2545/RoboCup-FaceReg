import face_recognition
import cv2
import numpy as np
import pickle
import os

def load_encodings(db_path):
    encodings = []
    names = []
    for file in os.listdir(db_path):
        if(file.endswith(".pickle")):
            with open(os.path.join(db_path,file), "rb") as f:
                encoding = pickle.load(f)
                encodings.append(encoding)
                names.append(file.replace(".pickle",""))
    return encodings, names

class RAFaceRecognition:
    def __init__(self, db_path):
        """
        Initialize RAFaceRecognition object

        :param db_path: path to database for storing face encodings
        """
        self.db_path = db_path
        self.face_encodings_db, self.names_db = load_encodings(db_path)
        print("loaded ", len(self.face_encodings_db), " encodings of ", self.names_db)

    def register(self, name, img):
        """
        Registers the most significant face in the img as encodings to the db_path folder

        :param name: register name
        :param img: 2D array Image
        :return: {message: string, isOk: boolean}
        """
        if(name in self.names_db): return {"message": "name taken", "isOk": False}
        try:
            encoding = face_recognition.face_encodings(img)[0]
            with open(os.path.join(self.db_path, name+".pickle"), "wb") as f:
                pickle.dump(encoding, f)
            return {"message": "Ok", "isOk": True}
        except:
            return {"message": "something wrong with the image", "isOk": False}

    def detectFace(self, img):
        """
        Detect a face/ faces in the image

        :param img: 2D array Image
        :return: return a dictionary of { name: (top, right, bottom, left) }
        """
        faces = {}
        if len(self.face_encodings_db) == 0: return faces

        small_img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_img[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for index, encoding in enumerate(encodings):
            matches = face_recognition.compare_faces(self.face_encodings_db, encoding)
            face_distances = face_recognition.face_distance(self.face_encodings_db, encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.names_db[best_match_index]
                (top, right, bottom, left) = face_locations[index]
                if name not in faces:
                    faces[name] = (top*4, right*4, bottom*4, left*4)

        return faces


if __name__ == "__main__":
    raFaceRecognition = RAFaceRecognition(db_path="database")
