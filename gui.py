import os
import tkinter as tk
import cv2
import numpy as np
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import customtkinter as ctk

class FolderImageSelector(ctk.CTk):
    def __init__(self, execute_callback):
        super().__init__()
        self.geometry("1x1")
        
        self.title("Folder and Image Selector")
        
        self.folder_path = None
        self.image_path = None
        self.execute_callback = execute_callback

        # Create a frame for the left side
        self.big_frame = ctk.CTkFrame(self)
        #self.big_frame.configure(fg_color="white")
        self.big_frame.pack(fill="both", expand=True)
        #self.big_frame.grid_rowconfigure(0, weight=1)  # configure grid system
        #self.big_frame.grid_columnconfigure(0, weight=0)
        #self.big_frame.grid_columnconfigure(1, weight=1)
        #self.big_frame.grid(row=0, column=0, sticky="news")
        self.left_frame = ctk.CTkFrame(self.big_frame)
        #self.big_frame.propagate(0)
        #self.left_frame.propagate(0)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
        #self.left_frame.pack(fill="both", expand=True)

        # Folder selection
        folder_label = ctk.CTkLabel(self.left_frame, text="Training folder:", anchor='w')
        folder_label.grid(row=0, column=0, padx=10, pady=20, sticky="e")
        
        self.folder_entry = ctk.CTkEntry(self.left_frame, placeholder_text="path for training folder")
        self.folder_entry.grid(row=0, column=1, sticky="we")
        
        folder_button = ctk.CTkButton(self.left_frame, text="Browse...", command=self.select_folder,
                          width=50)
        folder_button.grid(row=0, column=2, padx=10, pady=20)
        
        # Image selection
        image_label = ctk.CTkLabel(self.left_frame, text="Test image:", anchor='e')
        image_label.grid(row=1, column=0, padx=10, pady=20, sticky="e")
        
        self.image_entry = ctk.CTkEntry(self.left_frame, placeholder_text="path for image for testing",
        )
        self.image_entry.grid(row=1, column=1, sticky="we")
        
        image_button = ctk.CTkButton(self.left_frame, text="Browse...", command=self.select_image, 
                         width=50)
        image_button.grid(row=1, column=2, padx=10, pady=20)
        
        # Execute button
        execute_button = ctk.CTkButton(self.left_frame, text="Execute", command=self.execute_function)
        execute_button.grid(row=2, column=0, columnspan=3, pady=20)
        #self.left_frame.grid_propagate(False)
        # Create a frame for the right side
        self.right_frame = ctk.CTkFrame(self.big_frame)
        self.right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="news")
        self.right_frame.grid_remove()
        # Labels for images
        self.test_image_text = ctk.CTkLabel(self.right_frame, text="")
        self.test_image_text.grid(row=0, column=0, padx=10, pady=5)

        # Test Image Display
        self.input_image_label = ctk.CTkLabel(self.right_frame, text="")
        self.input_image_label.grid(row=1, column=0, padx=10, pady=5)

        self.result_image_text = ctk.CTkLabel(self.right_frame, text="")
        self.result_image_text.grid(row=0, column=1, padx=10, pady=5)
        self.result_image_text.grid_remove()
        # Result Image display
        self.result_image_label = ctk.CTkLabel(self.right_frame, text="")
        self.result_image_label.grid(row=1, column=1, padx=10, pady=5)
        self.result_image_label.grid_remove()
        
        self.not_found_label = ctk.CTkLabel(self.left_frame, text="")
        self.not_found_label.grid(row=2, column=0)
        self.not_found_label.grid_remove()

        self.error_label = ctk.CTkLabel(self.left_frame, text="")
        self.error_label.grid(row=3, column=0)
        self.error_label.grid_remove()

        #self.big_frame.grid_columnconfigure(0, weight=1)
        #self.big_frame.grid_columnconfigure(1, weight=1)
        #self.grid_columnconfigure(0, weight=1)
        #self.grid_rowconfigure(0, weight=1)
        #self.big_frame.propagate(0)
        #self.right_frame.propagate(0)
        self.update_size()
    
    def update_size(self):
        self.big_frame.update_idletasks()
        width = self.big_frame.winfo_reqwidth() - 90
        height = self.big_frame.winfo_reqheight() - 60
        if(self.right_frame.winfo_ismapped()):
            height -= 40
            width -= 75
            if(self.result_image_label.winfo_ismapped()):
                width -= 75

        self.geometry(f"{width}x{height}")

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, folder_path)
            self.update_size()
    
    def select_image(self):
        image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp")])
        if image_path:
            self.image_entry.delete(0, tk.END)
            self.image_entry.insert(0, image_path)
            self.result_image_label.configure(image="")
            self.result_image_label.grid_remove()
            self.result_image_text.configure(text="")
            self.result_image_text.grid_remove()
            self.show_image(image_path)
            self.right_frame.grid()
            self.error_label.grid_remove()
            self.not_found_label.grid_remove()
        #else:
        #    self.right_frame.grid_remove()
         
        self.result_image_label.configure(image="")
        self.result_image_text.configure(text="")
        self.update_size()

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
        img = cv2.resize(img, (336, 384))  
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(image=img)
        #self.result_image_label.grid()
        #self.result_image_text.grid()
        self.input_image_label.configure(image=img)
        self.input_image_label.image = img
        self.test_image_text.configure(text="Test Image")
        self.update_size()

    def show_image_by_id(self, folder_path, image_id):

        image_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp'))])
        
        if 0 <= image_id < len(image_files):
            image_path = os.path.join(folder_path, image_files[image_id])
            img = cv2.imread(image_path)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
            img = cv2.resize(img, (336, 384))  
            img = Image.fromarray(img)
            img = ImageTk.PhotoImage(image=img)
            self.result_image_label.grid()
            self.result_image_text.grid()
            self.result_image_label.configure(image=img)
            self.result_image_label.image = img 
            self.result_image_text.configure(text="Indentified Image")
            self.update_size()
            #self.test_image_text.configure(text="Indentifie")
        else:
            self.result_image_label.configure(image="")
            self.result_image_text.configure(text="")
            self.result_image_label.grid_remove()
            self.result_image_text.grid_remove()
            self.update_size()
            #self.test_image_text.configure(text="Indent


    def show_not_found_label(self, message):
        self.not_found_label.configure(text=message)
        self.not_found_label.grid()

    def show_error(self, error):
        self.error_label.configure(text=f"Erro: {error:.2f}".replace('.', ','))
        self.error_label.grid()
