"""All Imports in"""

import tkinter as tk 
from tkinter import ttk, scrolledtext 
from tkinter import messagebox as mBox
import connect
import models
from models import Products, Favorits, Cat
import pymysql.cursors

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
        self.cursor = connect.cursor
        # Add a title
        self.win.title("OpenFoodFacts")
        #creat widgets
        self.createWidgets()
        #self.insert_combox(values)
        self.win.resizable(0,0)
        #tuple of products combobox
        self.prods_val = ()
        
    
    
    def get_products(self):
        
        #----------------------- Geting the products--------------------------
        name = self.combo_cat.get()# Get datas from the categories  combobox
        self.get_id2 = self.cat.get_to_comboprods + "cat_name ='{}'".format(str(name))# Qery to get the id of the categorie name selected
        self.cursor.execute(self.get_id2)# execute the qery
        got = self.cursor.fetchall()# get the value of the qery with fetch()
        self.GUI_products = self.prods.combo_prods_get + "id_cat = {}".format(got[0]["id"]) # qery to get products linked to the specific categorie
        self.cursor.execute(self.GUI_products)
        self.geting = self.cursor.fetchall()# fetch the qery and get the products
         
        print(self.geting)
        
        #--------------- SHow products INfos ------------------------------
            
            
    def createWidgets(self):
        """This Method where widgets are created"""
        
        # Tabs's Control
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
        self.combo_cat = ttk.Combobox(self.monty, width=14)
        self.combo_cat.grid(column=1, row=0) 
        ttk.Label(self.monty, text="Choisir catégorie :").grid(column=0, row=0,sticky='W')
        
        # Product's widgets
        self.combo_prods = ttk.Spinbox(self.monty, width=30)
        self.combo_prods.grid(column=4, row=0) 
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
        
        #creating buttons
        # Geting products button
        self.get_prods = ttk.Button(self.monty, text = "obtenir_produits", command = self.get_products)
        self.get_prods.grid(column = 1, row = 4)
        #exit button
        self.exit = ttk.Button(self.monty, text = "Quitter", command = self.win.destroy)
        self.exit.grid(column = 2, row = 4)
        # sauvgarde button
        self.exit = ttk.Button(self.monty, text = "Enregistrer", command = self.win.destroy)
        self.exit.grid(column = 3, row = 4)
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
        """    
    
        #---------------------------------------tab's 2 widgets---------------------------
        