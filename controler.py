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
            
        self.req = requests.get(BOISSON_URL)
        self.result = self.req.json() 

    def Testing(self):
        print(self.req.status_code)

        
    def insert_in(self):
        pass



class ModelMy():
    
    def __init__(self):
        self.cursor = connect.cursor
        self.cat = Cat()
        self.prods = Products()
        
    def CreatMyClass(self):
        #self.cursor.execute(self.cat.creat)
        #self.cursor.execute(self.prods.creat)
        self.cursor.executemany(self.cat.insert, self.cat.val)
        connect.db.commit()



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

in_modelmy = ModelMy()
in_modelmy.CreatMyClass()




in_view = ViewMy()