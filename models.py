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
        
    def Cleanclass(self, nom_table):
        self.drop_class = "DROP TABLE " + nom_table
        self.cursor.execute(self.drop_class)

"""Models Classes"""

class Products():
    
    """This class present the products table """
    def __init__(self):
        self.cursor = connect.cursor
        # creating the table products
        self.sql = "CREATE TABLE "+ T_PRODS +" (id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, product_name VARCHAR(100) NOT NULL, id_cat SMALLINT, stores_name VARCHAR(100), nutri_score VARCHAR(120), description VARCHAR(3500), link VARCHAR(255), CONSTRAINT fk_id_cat FOREIGN KEY (id_cat) REFERENCES categories(id)) CHARSET= UTF8MB4 " 
        # geting the id of every categories names in the table categories
        self.get_id = "SELECT id FROM categories WHERE cat_name = 'charcutries' " 
        # inserting datas from the OFF's api
        self.insert_data = "INSERT INTO products (product_name, id_cat, stores_name, nutri_score, description, link) VALUES (%s, %s, %s, %s, %s, %s)" 
        #Multiple Selection linked to the view
        self.list_prods_name = "SELECT product_name FROM products WHERE "
        self.list_prods_link = "SELECT link FROM products WHERE "
        self.list_prods_nt = "SELECT nutri_score FROM products WHERE "
        self.list_prods_mag = "SELECT stores_name FROM products WHERE "
        self.list_prods_desc = "SELECT description FROM products WHERE "
        
        
        
    def create(self):
        """Method to creat table products """
        self.cursor.execute(self.sql)
     
        
        
    
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
        self.get_to_comboprods = "SELECT id FROM categories WHERE "
    def creat(self):
        """Method to creat table """
        self.cursor.execute(self.sql)
     
     
    def insert(self):
        """Method to insert values in the table categories"""
        self.cursor.executemany(self.sql_insert, self.val)
    
     