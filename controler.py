import views
from views import MyApp
import models
from models import *
import requests
import pymysql.cursors
import tkinter as tk # 1 imports
from tkinter import *
from tkinter import ttk 
from tkinter import scrolledtext
from tkinter import messagebox as mBox
import connect



"""Starting Classes"""

class ModelMy():
    
    def __init__(self):
            
        self.req = requests.get("https://fr.openfoodfacts.org/categorie/riz-souffle.json")
        self.result = self.req.json() 

    def Testing(self):
        print(self.req.status_code)







class ViewMy():
    pass









"""View run and execution"""

run_it = views.MyApp()
run_it.win.mainloop()

"""Model run and execution"""

run_model = models.MyBase()
run_model.CreatMyDB()

"""Local controler class execution"""

in_model = ModelMy()
in_model.Testing()

in_view = ViewMy()