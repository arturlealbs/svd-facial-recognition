from face_recognition import FaceRecognition
from gui import create_gui
import cv2

if __name__ == "__main__":
    create_gui()
    training_folder = 'images/training_folder'
    test_image_path = 'images/test.jpg'
    
    # Define a suitable threshold for known faces --> 100
    # Define a suitable threshold for face space --> 200
    face_recognition = FaceRecognition(training_folder, threshold_0=100, threshold_1=200) 

    test_image = cv2.imread(test_image_path, cv2.IMREAD_GRAYSCALE)
    identified_face = face_recognition.identify_face(test_image)

    print(identified_face)