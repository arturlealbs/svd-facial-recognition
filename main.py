import tkinter as tk
import cv2
from face_recognition import FaceRecognition
from gui import FolderImageSelector

if __name__ == "__main__":
    def execute_face_recognition(training_folder_path, test_image_path):

        # Define a suitable threshold for known faces --> 100
        # Define a suitable threshold for face space --> 200
        face_recognition = FaceRecognition(training_folder_path, threshold_0=10, threshold_1=200) 

        test_image = cv2.imread(test_image_path, cv2.IMREAD_GRAYSCALE)
        identified_face = face_recognition.identify_face(test_image)

        print(identified_face)

    app = FolderImageSelector(execute_callback=execute_face_recognition)
    app.mainloop()

