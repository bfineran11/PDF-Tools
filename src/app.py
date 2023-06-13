import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("PDF Tools")
        self.geometry("600x400")