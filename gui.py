import os
import tkinter as tk
import cv2
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


class FolderImageSelector(tk.Tk):
    def __init__(self, execute_callback):
        super().__init__()
        
        self.title("Folder and Image Selector")
        
        self.folder_path = None
        self.image_path = None
        self.execute_callback = execute_callback

        # Folder selection
        folder_label = tk.Label(self, text="Select Folder:")
        folder_label.grid(row=0, column=0, padx=10, pady=5)
        
        self.folder_entry = tk.Entry(self, width=50)
        self.folder_entry.grid(row=0, column=1, padx=10, pady=5)
        
        folder_button = tk.Button(self, text="Browse...", command=self.select_folder)
        folder_button.grid(row=0, column=2, padx=10, pady=5)
        
        # Image selection
        image_label = tk.Label(self, text="Select Image:")
        image_label.grid(row=1, column=0, padx=10, pady=5)
        
        self.image_entry = tk.Entry(self, width=50)
        self.image_entry.grid(row=1, column=1, padx=10, pady=5)
        
        image_button = tk.Button(self, text="Browse...", command=self.select_image)
        image_button.grid(row=1, column=2, padx=10, pady=5)
        
        # Execute button
        execute_button = tk.Button(self, text="Execute", command=self.execute_function)
        execute_button.grid(row=2, column=0, columnspan=3, pady=10)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.not_found_label = tk.Label(self)
        self.not_found_label.grid(row=3, column=1)

        # Labels for images
        self.test_image_text = tk.Label(self)
        self.test_image_text.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

        self.result_image_text = tk.Label(self)
        self.result_image_text.grid(row=5, column=0, columnspan=3, padx=10, pady=5)

        # Test Image Display
        self.input_image_label = tk.Label(self)
        self.input_image_label.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

        # Result Image display
        self.result_image_label = tk.Label(self)
        self.result_image_label.grid(row=6, column=0, columnspan=3, padx=10, pady=5)

        self.error_label = tk.Label(self)
        self.error_label.grid(row=7, column=1)

    
    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, folder_path)
    
    def select_image(self):
        image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")])
        if image_path:
            self.image_entry.delete(0, tk.END)
            self.image_entry.insert(0, image_path)
    
    def execute_function(self):
        if self.folder_entry.get() and self.image_entry.get():
            self.folder_path = self.folder_entry.get()
            self.image_path = self.image_entry.get()
            self.execute_callback(self.folder_path, self.image_path, self)
        else:
            messagebox.showwarning("Warning", "Please select both a folder and an image.")
    
    def show_image(self, image_path):
        img = cv2.imread(image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
        img = cv2.resize(img, (400, 400))  
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(image=img)

        self.input_image_label.config(image=img)
        self.input_image_label.image = img
        self.test_image_text.config(text="Imagem de Teste")

    def show_image_by_id(self, folder_path, image_id):

        image_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp'))])
        
        if 0 <= image_id < len(image_files):
            image_path = os.path.join(folder_path, image_files[image_id])
            img = cv2.imread(image_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
            img = cv2.resize(img, (400, 400))  
            img = Image.fromarray(img)
            img = ImageTk.PhotoImage(image=img)
            
            self.result_image_label.config(image=img)
            self.result_image_label.image = img 
            self.result_image_text.config(text="Rosto Identificado")

    def show_not_found_label(self, message):
        self.not_found_label.config(text=message)

    def show_error(self, error):
        self.error_label.config(text=f"Erro: {error:.2f}".replace('.', ','))