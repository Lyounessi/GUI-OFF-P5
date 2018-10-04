"""All Imports in"""

import tkinter as tk # 1 imports
from tkinter import *
from tkinter import ttk 
from tkinter import scrolledtext
from tkinter import messagebox as mBox


"""Class content all widgets indeed"""
#The new OOP code looks like this:
class MyApp():
    
    def __init__(self):
        # Create instance
        self.win = tk.Tk()

        # Add a title
        self.win.title("Python GUI")
        self.createWidgets()

    # … more callback methods
    def createWidgets(self):
        # Tab Control introduced here -----------------------
        tabControl = ttk.Notebook(self.win) # Create Tab Control

        tab1 = ttk.Frame(tabControl) # Create a tab
        tabControl.add(tab1, text='Tab 1') # Add the tab
        
        tab2 = ttk.Frame(tabControl) # Create second tab
        tabControl.add(tab2, text='Tab 2') # Add second tab
        tabControl.pack(expand=1, fill="both") # Pack make visible
        
    
