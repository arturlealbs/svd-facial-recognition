import cv2
from face_recognition import FaceRecognition
from gui import FolderImageSelector

if __name__ == "__main__":
    def execute_face_recognition(training_folder_path, test_image_path, gui):
        face_recognition = FaceRecognition(training_folder_path, threshold_0=6000, threshold_1=3000)

        test_image = cv2.imread(test_image_path, cv2.IMREAD_GRAYSCALE)
        test_image = cv2.equalizeHist(test_image)
        identified_face, error = face_recognition.identify_face(test_image)

        print(f"Identified face ID: {identified_face}")

        if type(identified_face) is str:
            gui.show_not_found_label(identified_face)
        else:
            gui.show_image(test_image_path)
            gui.show_image_by_id(training_folder_path, identified_face)
            gui.show_error(error)
    
    app = FolderImageSelector(execute_callback=execute_face_recognition)
    app.mainloop()

