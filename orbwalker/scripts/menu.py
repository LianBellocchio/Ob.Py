import tkinter as tk

class Menu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Menu")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        self.menu_frame = tk.Frame(self.root, bg="#0f1923", padx=10, pady=10)
        self.menu_frame.pack(fill=tk.BOTH, expand=True)
        
        self.title_label = tk.Label(self.menu_frame, text="Menu", fg="white", bg="#0f1923", font=("Arial", 16))
        self.title_label.pack(pady=10)
        
        self.start_button = tk.Button(self.menu_frame, text="Start", width=30, height=2, bg="#3c5c79", fg="white", font=("Arial", 14))
        self.start_button.pack(pady=10)
        
        self.config_button = tk.Button(self.menu_frame, text="Configuration", width=30, height=2, bg="#3c5c79", fg="white", font=("Arial", 14))
        self.config_button.pack(pady=10)
        
        self.quit_button = tk.Button(self.menu_frame, text="Quit", width=30, height=2, bg="#3c5c79", fg="white", font=("Arial", 14), command=self.root.destroy)
        self.quit_button.pack(pady=10)
        
        self.root.bind("<Escape>", lambda event: self.root.destroy())
        self.root.bind("<Shift-Left>", lambda event: self.root.lift())
        
    def run(self):
        self.root.mainloop()
