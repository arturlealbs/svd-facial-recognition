import cv2
import numpy as np
import os
import svd

class FaceRecognition:
    def __init__(self, training_folder, threshold_0=100, threshold_1=500):
        self.training_folder = training_folder
        self.threshold_0 = threshold_0
        self.threshold_1 = threshold_1
        self.mean_face = None
        self.U = None
        self.coordinate_vectors = None
        self.load_training_data()

    def load_images_from_folder(self, folder):
        images = []
        for filename in os.listdir(folder):
            img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
            if img is not None:
                images.append(img.flatten())
        return images

    def compute_mean_face(self, A):
        return np.mean(A, axis=1)

    def compute_svd(self, A, mean_face):
        A_centered = A - mean_face[:, None]
        return np.linalg.svd(A_centered, full_matrices=False)
        #return svd.svd(A_centered)

    def compute_coordinate_vectors(self, U, A, mean_face):
        A_centered = A - mean_face[:, None]
        return U.T @ A_centered

    def load_training_data(self):
        training_images = self.load_images_from_folder(self.training_folder)
        A = np.array(training_images).T
        self.mean_face = self.compute_mean_face(A)
        self.U, _, _ = self.compute_svd(A, self.mean_face)
        self.coordinate_vectors = self.compute_coordinate_vectors(self.U, A, self.mean_face)

    def identify_face(self, test_image):
        test_image_flat = test_image.flatten()
        test_image_centered = test_image_flat - self.mean_face
        x = self.U.T @ test_image_centered
        pf = self.U @ x
        ef = np.linalg.norm(test_image_centered - pf)
        ### tem esse threshold  
        ## esse valor do ef tá entre 300 e 500
        ## ent thresshold 1 fica sendo 500
        if ef > self.threshold_1:
            print(ef)
            return "Not a face"

        distances = np.linalg.norm(self.coordinate_vectors - x[:, None], axis=0)
        min_distance = np.min(distances)

        ## essa distância tá nos 3000
        ## o que era para ser cada um? 
        print(min_distance)
        if min_distance < self.threshold_0:
            return np.argmin(distances)
        else:
            return "Unknown face"