"""Imports Parts"""
#Views Imports
import views
from views import MyApp

#Models Imports
import models
from models import *


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
from constant import *


"""Starting Classes"""

        



class ModelMy():
    
    def __init__(self):
        self.cursor = connect.cursor
        self.cat = models.Cat()
        self.prods = models.Products()
        
    def CreatMyClass(self):
        #self.cat.creat()
        #self.prods.create()
        connect.db.commit()
    
    def insertion(self):
        self.cat.insert()
        connect.db.commit()
       
        



class ViewMy():
    pass



"""View run and execution"""

run_it = views.MyApp()
run_it.win.mainloop()

"""Model run and execution"""

run_model = models.MyBase()
#run_model.CreatMyDB()

in_modelmy = ModelMy()
in_modelmy.CreatMyClass()
in_modelmy.insertion()



