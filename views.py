"""All Imports in"""

import tkinter as tk 
from tkinter import ttk, scrolledtext, Scrollbar, END, ACTIVE
from tkinter import Listbox as lb
import connect
import models
from models import Products, Favorits, Cat
import pymysql.cursors
import webbrowser
 
"""Class content all widgets indeed"""
#The new OOP code looks like this:
class MyApp():
    """This is the global class, making the view and all widgets inside"""
    def __init__(self):

        # Create instances
        self.win = tk.Tk()
        self.win.iconbitmap(r'C:\Users\boukr\Desktop\here\GUI-OFF-P5\logo.ico')
        #Attributs of the models's Classes
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
        #define the attribut text for lables
        
        
    
    
    def get_products(self):
        """Method Geting the products"""
        
        name = self.combo_cat.get()# Get datas from the categories  combobox
        self.get_id2 = self.cat.get_to_comboprods + "cat_name ='{}'".format(str(name))# Qery to get the id of the categorie name selected
        self.cursor.execute(self.get_id2)# execute the qery
        got = self.cursor.fetchall()# get the value of the qery with fetch()
        self.GUI_products = self.prods.list_prods_name + "id_cat = {}".format(got[0]["id"]) # qery to get products linked to the specific categorie's id
        self.cursor.execute(self.GUI_products)
        self.geting = self.cursor.fetchall()# fetch the qery and get the products
        self.list_prods.delete(0, tk.END)
        for prods in self.geting:
            self.list_prods.insert(0, prods["product_name"])
    
    def getprodinfos(self):
        """Method to show products Infos"""
        
        name = self.list_prods.get(ACTIVE)
        self.name_lab["text"] = name #get the name of product from the listbox directly
        # preparing querys
        link = self.prods.list_prods_link + "product_name = '{}'".format(str(name))
        nutri_score = self.prods.list_prods_nt + "product_name = '{}'".format(str(name))
        mags = self.prods.list_prods_mag + "product_name = '{}'".format(str(name))
        desc = self.prods.list_prods_desc + "product_name = '{}'".format(str(name))
        #execute querys
        exe_link = self.cursor.execute(link)
        link_get = self.cursor.fetchone()
        exe_ns = self.cursor.execute(nutri_score)
        nutri_get = self.cursor.fetchone()
        exe_mags = self.cursor.execute(mags)
        mag_get = self.cursor.fetchone()
        #get infos
        self.link_lab["text"] = link_get["link"]
                                
        
        
            
    def createWidgets(self):
        """This Method where widgets are created"""
        
        # Tabs's Control
        tabControl = ttk.Notebook(self.win) 

        tab1 = ttk.Frame(tabControl) 
        tabControl.add(tab1, text='Produits') 
        tabControl.pack(expand=1, fill="both")
        # Create second tab
        tab2 = ttk.Frame(tabControl) 
        tabControl.add(tab2, text='Favorits') # Add second tab
        tabControl.pack(expand=1, fill="both") # Pack make visible
        
         # ----------------------Tabe's1 widgets---------------------------
        self.monty = ttk.LabelFrame(tab1, text=' Liste des Produits ')
        self.monty.pack()
        ttk.Label(self.monty, text="Choisir catégorie :").pack()
        
        # widgets of the categories
        self.combo_cat = ttk.Combobox(self.monty, width=14)
        self.combo_cat.pack()
        ttk.Label(self.monty, text="Choisir produit :").pack()
        
        # Product's widgets
        scroll = Scrollbar(self.monty, orient="vertical")
        self.list_prods = lb(self.monty, xscrollcommand = scroll, width= 40, height = 15)
        self.list_prods.pack()
        
        
        #Labels Groups
        font_size = 12
        #name
        self.name_lab = ttk.Label(self.monty, text= "NOM PRODUIT", font=("Helvetica", font_size))
        self.name_lab.pack()
        
        #Link
        self.link_lab = ttk.Label(self.monty, text=r"LIEN", font=("Helvetica", font_size))
        self.link_lab.pack()
        
        #nutrition_score
        self.nt_lab = ttk.Label(self.monty, text="NUTRI SCORE", font=("Helvetica", font_size))
        self.nt_lab.pack()
        
        #store_name
        self.store_lab = ttk.Label(self.monty, text="MAGASIN", font=("Helvetica", font_size))
        self.store_lab.pack()
        
        #Description of the product(ingredients) by scrolled text
        ttk.Label(self.monty, text="Description_ingredients :").pack()
        scrol_w = 50
        scrol_h = 3
        src = scrolledtext.ScrolledText(self.monty, width = scrol_w, height = scrol_h, wrap = tk.WORD)
        src.pack()
        
        #creating buttons
        b_width = 30
        # Geting products button
        self.get_prods = ttk.Button(self.monty, text = "obtenir_produits", width = b_width, command = self.get_products)
        self.get_prods.pack()
        #exit button
        self.exit = ttk.Button(self.monty, text = "Quitter", width = b_width, command = self.win.destroy)
        self.exit.pack()
        #informations about products button
        self.exit = ttk.Button(self.monty, text = "infos_produit", width = b_width, command = self.getprodinfos)
        self.exit.pack()
        # sauvgarde button
        self.exit = ttk.Button(self.monty, text = "Enregistrer", width = b_width, command = self.win.destroy)
        self.exit.pack()
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
        