"""Imports Parts"""
import pymysql.cursors
import json
import connect
from connect import cursor
import constant 
from constant import *
#import controler
#from controler import ModelMy

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
    
    """This class present the products table """
    def __init__(self):
        self.cursor = connect.cursor
        self.sql = "CREATE TABLE "+ T_PRODS +" (id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, product_name VARCHAR(100) NOT NULL, id_cat SMALLINT, stores_name VARCHAR(100), nutri_score VARCHAR(120), description VARCHAR(3500), link VARCHAR(255), CONSTRAINT fk_id_cat FOREIGN KEY (id_cat) REFERENCES categories(id)) CHARSET= UTF8MB4 "
        self.get_id = "SELECT id FROM categories WHERE cat_name = 'Charcutries' "
        self.insert_data = "INSERT INTO products (product_name, id_cat, stores_name, nutri_score, description, link) VALUES (%s, %s, %s, %s, %s, %s)"
        
        
        
    def create(self):
        
        self.cursor.execute(self.sql)
    
    def show_data(self, info_to_show):
        self.show = "SELECT "+info_to_show+" FROM products"
        self.cursor.execut(self.show)
        self.cursor.fetchone(self.show)
     
    
    
        
        
    
class Favorits():
    
    """This class present the favorits table """
    def __init__(self):
        pass
       
    def create(self):
        pass
     
     
    def insert(self):
        
        pass
    
    
class Cat():
    """This class present the categories table """
    def __init__(self):
        
        self.cursor = connect.cursor
        self.sql = "CREATE TABLE "+ T_CAT +" (id SMALLINT AUTO_INCREMENT, cat_name VARCHAR(55) NOT NULL, PRIMARY KEY (id))"
        self.sql_insert = "INSERT INTO "+ T_CAT+"(cat_name) VALUES (%s)" 
        self.val=[('Fromages'),('Charcutries'),('Produits à tartiner'),('Boissons')]
        self.get_cats = "SELECT cat_name FROM categories"    

    def creat(self):
        self.cursor.execute(self.sql)
     
     
    def insert(self):
        self.cursor.executemany(self.sql_insert, self.val)
    
     