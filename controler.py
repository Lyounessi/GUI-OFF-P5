"""Imports Parts"""

import views
from views import MyApp
import models
from models import *
from models import Cat
import requests
import pymysql.cursors
import tkinter as tk # 1 imports
from tkinter import *
from tkinter import ttk 
from tkinter import scrolledtext
from tkinter import messagebox as mBox
import connect
import constant
from constant import *


"""Starting Classes"""
class ApiMy():
    def __init__(self):
        self.cursorr = connect.cursor
        self.req = requests.get(BOISSON_URL)
        self.result = self.req.json()
        self.cat = Cat()
        self.my_products = []

    def Testing(self):
        print(self.req.status_code)
    
    
    def list_append(self):
        
        self.ex_for_key = 20
        #append data in the list:
        for i in range(20):
            self.my_products.extend([self.result["products"][i]["product_name"], int(self.ex_for_key), self.result["products"][i]["stores_tags"], self.result["products"][i]["nutrition_grades_tags"], self.result["products"][i]["ingredients_tags"],  self.result["products"][i]["url"]])
            
    def insert_in(self):
        self.sql = ""
        self.val = "" 
        
        print(self.ex_for_key)
        print(type(self.ex_for_key))
        for i in self.my_products:
            self.sql = "INSERT INTO products (product_name, id_cat, stores_name, nutri_score, description, link) VALUES ('%s', '%d', '%s', '%s', '%s', '%s')"
            self.val = (i)
            self.cursorr.executemany(self.sql, self.val)
        connect.db.commit()
            
        



class ModelMy():
    
    def __init__(self):
        self.cursor = connect.cursor
        self.cat = Cat()
        self.prods = Products()
        
    def CreatMyClass(self):
        #self.cursor.execute(self.cat.creat)
        #self.cursor.execute(self.prods.creat)
        self.cursor.executemany(self.cat.insert, self.cat.val)
        #connect.db.commit()
       
        



class ViewMy():
    pass


print('yes')

"""View run and execution"""

run_it = views.MyApp()
run_it.win.mainloop()

"""Model run and execution"""

run_model = models.MyBase()
#run_model.CreatMyDB()

"""Local controler class execution"""

in_api = ApiMy()
in_api.Testing()
in_api.list_append()
in_api.insert_in()


in_modelmy = ModelMy()
#in_modelmy.CreatMyClass()




in_view = ViewMy()