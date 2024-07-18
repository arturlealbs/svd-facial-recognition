import tkinter as tk
import cv2
from face_recognition import FaceRecognition
from gui import FolderImageSelector

if __name__ == "__main__":
    def execute_face_recognition(training_folder_path, test_image_path):
        face_recognition = FaceRecognition(training_folder_path, threshold_0=100, threshold_1=500) 

        test_image = cv2.imread(test_image_path, cv2.IMREAD_GRAYSCALE)
        identified_face = face_recognition.identify_face(test_image)

        print(identified_face)

    app = FolderImageSelector(execute_callback=execute_face_recognition)
    app.mainloop()

