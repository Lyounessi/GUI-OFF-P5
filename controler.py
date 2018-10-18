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
import urllib.parse
from constant import *


"""Starting Classes"""

        



class ModelMy():
    
    def __init__(self):
        self.cursor = connect.cursor
        self.cat = models.Cat()
        self.prods = models.Products()
        
        #requests and api
        self.req = requests.get(self.Creat_url('saucissons'))
        self.data_prods = []
        
        
    def Creat_url(self, nom_categorie):
    
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
        my_req = self.req.json()
        prods = my_req["products"]
        
        #Makin the list global for using in all functions
        global data_prods
       
        
        self.cursor.execute(self.prods.get_id)
        got = self.cursor.fetchall()
        print(got[0]["id"])
        
        for i in range(20):
            val = (prods[i]["product_name"], int(got[0]["id"]), ''.join(prods[i]["stores_tags"]), ''.join(prods[i]["nutrition_grades_tags"]), ''.join(prods[i]["ingredients_tags"]), prods[i]["url"])
            self.cursor.execute(self.prods.insert_data, val)
            
        connect.db.commit()
    
    
    
        
        
    



class ViewMy():
    pass



"""View run and execution"""

run_it = views.MyApp()
run_it.win.mainloop()

"""Model run and execution"""

#run_model = models.MyBase()
#run_model.CreatMyDB()

in_modelmy = ModelMy()
in_modelmy.CreatMyClass()
in_modelmy.Get_Insert_products()