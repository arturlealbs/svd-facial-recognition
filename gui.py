import tkinter as tk
from tkinter import filedialog, messagebox

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
        execute_button.grid(row=2, columnspan=3, pady=10)
    
    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, folder_path)
    
    def select_image(self):
        image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")])
        if image_path:
            self.image_entry.delete(0, tk.END)
            self.image_entry.insert(0, image_path)
    
    def execute_function(self):
        if self.folder_entry.get() and self.image_entry.get():
            self.folder_path = self.folder_entry.get()
            self.image_path = self.image_entry.get()
            self.execute_callback(self.folder_path, self.image_path)
        else:
            messagebox.showwarning("Warning", "Please select both a folder and an image.")
    
