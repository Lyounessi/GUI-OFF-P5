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

"""Starting Classes"""

class ModelMy():
    pass









class ViewMy():
    pass









"""View run and execution"""

run_it = views.MyApp()
run_it.win.mainloop()

"""Model run and execution"""

run_model = models.MyBase()
run_model.Creation()

"""Local controler class execution"""

in_model = ModelMy()

in_view = ViewMy()