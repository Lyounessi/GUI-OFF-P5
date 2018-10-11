"""All Imports in"""

import tkinter as tk # 1 imports
from tkinter import *
from tkinter import ttk 
from tkinter import scrolledtext
from tkinter import messagebox as mBox
import connect

"""Class content all widgets indeed"""
#The new OOP code looks like this:
class MyApp():
    
    def __init__(self):
        # Create instance
        self.win = tk.Tk()

        # Add a title
        self.win.title("Python GUI")
        self.createWidgets()
        self.win.resizable(0,0)
    # … more callback methods
    def createWidgets(self):
        # Tab Control introduced here -----------------------
        tabControl = ttk.Notebook(self.win) # Create Tab Control

        tab1 = ttk.Frame(tabControl) # Create a tab
        tabControl.add(tab1, text='Produits') # Add the tab
       
        
        
        
        tab2 = ttk.Frame(tabControl) # Create second tab
        tabControl.add(tab2, text='Favorits') # Add second tab
        tabControl.pack(expand=1, fill="both") # Pack make visible
        
         # Tabe1 widgets
        monty = ttk.LabelFrame(tab1, text=' Liste des Produits ')
        monty.grid(column=0, row=1, padx=8, pady=4)
        monty = ttk.LabelFrame(tab1, text=' Monty Python ')
        monty.grid(column=0, row=1, padx=8, pady=4)
        ttk.Label(monty, text="Choisir catégorie :").grid(column=0, row=0,sticky='W')
        
        # widgets of the categories
        combo_cat = ttk.Combobox(monty, width=14)
        combo_cat.grid(column=1, row=0) 
        ttk.Label(monty, text="Choisir catégorie :").grid(column=0, row=0,sticky='W')
        
        # Product's widgets
        combo_cat = ttk.Combobox(monty, width=14)
        combo_cat.grid(column=4, row=0) 
        ttk.Label(monty, text="Choisir Produit :").grid(column=3, row=0,sticky='W')
        
        #Labels Groups
        #name
        ttk.Label(monty, text="Nom :").grid(column=0, row=1,sticky='W')
        ttk.Label(monty, text="get name").grid(column=1, row=1,sticky='W')
        
        #Link
        ttk.Label(monty, text="Lien :").grid(column=0, row=2,sticky='W')
        ttk.Label(monty, text="get link").grid(column=1, row=2,sticky='W')
        
        #nutrition_score
        ttk.Label(monty, text="Nutrition_score :").grid(column=2, row=1,sticky='W')
        ttk.Label(monty, text="get NT").grid(column=3, row=1,sticky='E')
        
        #store_name
        ttk.Label(monty, text="Magasin :").grid(column=2, row=2,sticky='W')
        ttk.Label(monty, text="get store").grid(column=3, row=2,sticky='E')