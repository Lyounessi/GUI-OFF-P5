"""Imports Parts"""
#Views Imports
import views
from views import MyApp

#Models Imports
import models
from models import Cat, Products, MyBase



#Requests API Imports
import requests
import pymysql.cursors

#TK Imports
import tkinter as tk # 1 imports
from tkinter import *
from tkinter import ttk 
from tkinter import scrolledtext
from tkinter import messagebox as mBox

#connexion Import
import connect

#Constants import
import constant
# urllib python
import urllib.parse



"""Starting Classes"""

        



class ModelMy():
    
    def __init__(self):
        #define the cursor of pymysql to manipulate datas
        self.cursor = connect.cursor
        # creating objects that are imported from models
        self.cat = models.Cat()
        self.prods = models.Products()
        
        
        #Geting the link of a specific categorie mentionned "creat_url method"
        self.req = requests.get(self.Creat_url('saucissons'))
        
        
        
    def Creat_url(self, nom_categorie):
        """This method  creat the link of the api that is filtred by the categories using python urllib"""
        
        suffixe_url_element = {
        'action' : 'process',
        'tagtype_0' : 'categories',
        'tag_contains_0' : 'contains',
        'tag_0' : nom_categorie,
        'page_size' : '20',
        'page' : '1',
        'json' : '1'
        }
        prefixe_url = 'https://fr.openfoodfacts.org/cgi/search.pl?'

        url = prefixe_url + urllib.parse.urlencode(suffixe_url_element)
        return url    
        
    def CreatMyClass(self):
        #self.cat.creat()
        #self.prods.create()
        #connect.db.commit()
        pass

    
    def Get_Insert_products(self):
        #define the variabl that convert the api requests value as json format
        my_req = self.req.json()
        #define the key products that have all the data indeed as content inside the json dict
        prods = my_req["products"]
        
        #getting the id form categories table, situeted in the models
        self.cursor.execute(self.prods.get_id)
        got = self.cursor.fetchall()
        print(got[0]["id"])
        
        #execute the query of insert from models and insert all the specific data in the table products
        for i in range(20):
            val = (prods[i]["product_name"], int(got[0]["id"]), ''.join(prods[i]["stores_tags"]), ''.join(prods[i]["nutrition_grades_tags"]), ''.join(prods[i]["ingredients_tags"]), prods[i]["url"])
            self.cursor.execute(self.prods.insert_data, val)
            
        connect.db.commit()
    
    
        
        
        
    



class ViewMy():
    
    def __init__(self):
        #define the cursor of pymysql to manipulate datas
        self.cursor = connect.cursor
        #Geting all classes indeed
        self.cat = models.Cat()
        self.prods = models.Products()
        self.app = views.MyApp()
        #self.app.win.mainloop()
        #creat a tuple of categories value to add in the comobox of the view
        self.cats_val =()
        
    
    def GetData_ToCats(self):
        """This Method used to append data into the categorie's combobox in the view"""
        self.cursor.execute(self.cat.get_cats) # execute the query of selecting all datas from the categories
        my_cats = self.cursor.fetchall() # geting the value of the query
        self.cats_val =(my_cats[0]["cat_name"], my_cats[1]["cat_name"], my_cats[2]["cat_name"], my_cats[3]["cat_name"]) # making a tuple having the cat_name's datas
        
        for i in self.cats_val:
            print(i)

    def RuMe(self):
        self.app.win.mainloop()


"""Model run and execution"""

#run_model = models.MyBase()
#run_model.CreatMyDB()

#in_modelmy = ModelMy()
#in_modelmy.CreatMyClass()
#in_modelmy.Get_Insert_products()

"""View class runs"""
in_viewmy = ViewMy()
in_viewmy.GetData_ToCats()
in_viewmy.RuMe()