import face_recognition
import pickle
import os

def load_encodings(db_path):
    encodings = []
    for file in os.listdir(db_path):
        if(file.endswith(".pickle")):
            with open(os.path.join(db_path,file), "rb") as f:
                encoding = pickle.load(f)
                encodings.append(encoding)
    return encodings

class RAFaceRecognition:
    def __init__(self, db_path):
        self.db_path = db_path
        self.face_encodings_db = load_encodings(db_path)

    def register(self, name, img):
        """
        Registers name as encodings to the db_path folder

        :param name: register name
        :param img: 2D array of a face of the image
        :return: Boolean (True - Ok, False - Not Ok)
        """
        try:
            encoding = face_recognition.face_encodings(img)[0]
            with open(os.path.join(self.db_path, name+".pickle"), "wb") as f:
                pickle.dump(encoding, f)
            return True
        except:
            return False

if __name__ == "__main__":
    rafaceRecog = RAFaceRecognition("database")

