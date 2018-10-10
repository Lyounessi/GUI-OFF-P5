"""Imports Parts"""
import pymysql.cursors
import json
import connect
from connect import cursor
import constant 
from constant import *

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
        self.creat = "CREATE TABLE products (id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, product_name VARCHAR(100) NOT NULL, id_cat SMALLINT, stores_name VARCHAR(100), nutri_score VARCHAR(2), CONSTRAINT fk_id_cat FOREIGN KEY (id_cat) REFERENCES categories(id))"


class Favorits():
     def __init__(self):
        pass
       

class Cat():
     def __init__(self):
            self.creat = "CREATE TABLE categories (id SMALLINT AUTO_INCREMENT, cat_name VARCHAR(55) NOT NULL, PRIMARY KEY (id))"
            self.insert = "INSERT INTO "+ T_CAT+"(cat_name) VALUES (%s)" 
            self.val=[('Fromages'),('Charcutries'),('Produits à tartiner'),('Boissons')]