"""Imports Parts"""
import pymysql.cursors
import json
import connect
from connect import cursor

"""Starting Classes"""

class MyBase():
    
    def __init__(self):
        self.db = "CREATE DATABASE IF NOT EXISTS Off_data"   
        
        #Define cursor for pymysql controls
        self.cursor = connect.cursor
        
          
        
    def CreatMyDB(self):
        self.cursor.execute(self.db)

"""Models Classes"""

class Products():
    
    def __init__(self):
        pass


class Favorits():
     def __init__(self):
        pass
       

class Cat():
     def __init__(self):
            self.creat = "CREATE TABLE categories (id SMALLINT AUTO_INCREMENT, cat_name VARCHAR(55) NOT NULL, PRIMARY KEY (id))"