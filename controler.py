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



"""Starting Classes"""
class ApiMy():
    def __init__(self):
            
        self.req = requests.get("https://fr.openfoodfacts.org/categorie/riz-souffle.json")
        self.result = self.req.json() 

    def Testing(self):
        print(self.req.status_code)



class ModelMy():
    
    def __init__(self):
        self.cursor = connect.cursor
        self.cat = Cat()
        
        
    def CreatMyClass(self):
        self.cursor.execute(self.cat.creat)





class ViewMy():
    pass









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