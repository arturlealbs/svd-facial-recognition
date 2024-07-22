import tkinter as tk
import cv2
from face_recognition import FaceRecognition
from gui import FolderImageSelector

if __name__ == "__main__":
    def execute_face_recognition(training_folder_path, test_image_path, gui):
        face_recognition = FaceRecognition(training_folder_path, threshold_0=8500, threshold_1=10000) 

        test_image = cv2.imread(test_image_path, cv2.IMREAD_GRAYSCALE)
        identified_face = face_recognition.identify_face(test_image)

        print(f"Identified face ID: {identified_face}")

        if identified_face == "Not a face":
            #chamar função na gui que Escreve Not a Face
            pass
        elif identified_face == "Unknown face":
            #chamar a função na gui que escreve Unknow Face e mostra a Distância
            pass
        else:
            gui.show_image(test_image_path)
            gui.show_image_by_id(training_folder_path, identified_face)

            

    app = FolderImageSelector(execute_callback=execute_face_recognition)
    app.mainloop()

