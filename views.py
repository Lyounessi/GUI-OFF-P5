"""All Imports in"""

import tkinter as tk 
from tkinter import ttk, scrolledtext 
from tkinter import messagebox as mBox
import connect
import models
from models import Products, Favorits, Cat


"""Class content all widgets indeed"""
#The new OOP code looks like this:
class MyApp():
    """This is the global class, making the view and all widgets inside"""
    def __init__(self):

        # Create instances
        self.win = tk.Tk()
        self.win.iconbitmap(r'C:\Users\boukr\Desktop\here\GUI-OFF-P5\logo.ico')
        """Attributs of the models's Classes"""
        self.cat = models.Cat()
        self.prods = models.Products()
        self.fav = models.Favorits
        
        # Add a title
        self.win.title("OpenFoodFacts")
        self.createWidgets()
        #self.insert_combox(values)
        self.win.resizable(0,0)
        #widgets
        #self.combo_cat = ""
        #self.monty =""
        
        
    def createWidgets(self):
        # Tab Control
        tabControl = ttk.Notebook(self.win) 

        tab1 = ttk.Frame(tabControl) 
        tabControl.add(tab1, text='Produits') 
       
        # Create second tab
        tab2 = ttk.Frame(tabControl) 
        tabControl.add(tab2, text='Favorits') # Add second tab
        tabControl.pack(expand=1, fill="both") # Pack make visible
        
         # ----------------------Tabe's1 widgets---------------------------
        self.monty = ttk.LabelFrame(tab1, text=' Liste des Produits ')
        self.monty.grid(column=0, row=1, padx=8, pady=4)
        ttk.Label(self.monty, text="Choisir catégorie :").grid(column=0, row=0,sticky='W')
        
        # widgets of the categories
        self.combo_cat = ttk.Combobox(self.monty,  width=14)
        self.combo_cat.grid(column=1, row=0) 
        ttk.Label(self.monty, text="Choisir catégorie :").grid(column=0, row=0,sticky='W')
        
        # Product's widgets
        self.combo_cat = ttk.Combobox(self.monty, width=14)
        self.combo_cat.grid(column=4, row=0) 
        ttk.Label(self.monty, text="Choisir Produit :").grid(column=3, row=0,sticky='W')
        
        #Labels Groups
        #name
        ttk.Label(self.monty, text="Nom :").grid(column=0, row=1,sticky='W')
        ttk.Label(self.monty, text="get name").grid(column=1, row=1,sticky='W')
        
        #Link
        ttk.Label(self.monty, text="Lien :").grid(column=0, row=2,sticky='W')
        ttk.Label(self.monty, text="get link").grid(column=1, row=2,sticky='W')
        
        #nutrition_score
        ttk.Label(self.monty, text="Nutrition_score :").grid(column=2, row=1,sticky='W')
        ttk.Label(self.monty, text="get NT").grid(column=3, row=1,sticky='E')
        
        #store_name
        ttk.Label(self.monty, text="Magasin :").grid(column=2, row=2,sticky='W')
        ttk.Label(self.monty, text="get store").grid(column=3, row=2,sticky='E')
        
        #Description of the product(ingredients) by scrolled text
        ttk.Label(self.monty, text="Description_ingredients :").grid(column=1, row=3,sticky='W')
        scrol_w = 30
        scrol_h = 3
        src = scrolledtext.ScrolledText(self.monty, width = scrol_w, height = scrol_h, wrap = tk.WORD)
        src.grid(column = 2, row = 3)
        
        """
        #The second box (Lable_Frames) of the best products comparing
        
        #secon section in tab1 for best products
        monty1 = ttk.LabelFrame(tab1, text=' Meilleur Produit ')
        monty1.grid(column=0, row=5, padx=8, pady=4)
         
        #name
        ttk.Label(monty1, text="Nom :").grid(column=0, row=1,sticky='W')
        ttk.Label(monty1, text="get name").grid(column=2, row=1,sticky='W')
        
        #Link
        ttk.Label(monty1, text="Lien :").grid(column=0, row=2,sticky='W')
        ttk.Label(monty1, text="get link").grid(column=2, row=2,sticky='E')
        
        #nutrition_score
        ttk.Label(monty1, text="Nutrition_score :").grid(column=4, row=1,sticky='E')
        ttk.Label(monty1, text="get NT").grid(column=5, row=1,sticky='E')
        
        #store_name
        ttk.Label(monty1, text="Magasin :").grid(column=4, row=2,sticky='E')
        ttk.Label(monty1, text="get store").grid(column=5, row=2,sticky='E')
        
        
        def ShowProducts(self):
            pass
        """    
      