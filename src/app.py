from tkinter import *
from tkinter import ttk
import customtkinter

class MainWindow(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        # initializing / configuring window and tkinter
        customtkinter.CTk.__init__(self, *args, **kwargs)
        self.wm_title("PDF Tools")
        self.geometry("600x400")
        
        # frame where everything will be put
        mainframe = customtkinter.CTkFrame(self).place()
        
        # header label
        header_label = customtkinter.CTkLabel(mainframe, text="PDF Tools").grid()
        
        # Select File Button
        select_file_button = customtkinter.CTkButton(mainframe, text="Select File...").grid()
        
        
        """
        Operation Choice:
        
        When each button is selected, present ui that corresponds with info needed
        to carry out operation
        
        rm, destroy
        """
        # Choose operation radio buttons
        operation_choice = StringVar()
        
        # split pdf files
        split_pdf_rb = customtkinter.CTkRadioButton(mainframe, 
                                      text="Split PDF", 
                                      variable=operation_choice, 
                                      value="split").grid()
        
        # join pdf files
        join_pdf_rb = customtkinter.CTkRadioButton(mainframe, 
                                      text="Join PDF's", 
                                      variable=operation_choice, 
                                      value="join").grid()
        
        # remove pages
        rm_page_rb = customtkinter.CTkRadioButton(mainframe, 
                                      text="Remove Page(s)", 
                                      variable=operation_choice, 
                                      value="remove").grid()
        