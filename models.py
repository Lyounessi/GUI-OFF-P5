"""Imports Parts"""
import pymysql.cursors
import json


"""Starting Classes"""

class MyBase():
    
    def __init__(self):
        # creat connection to the server
        self.conect = pymysql.connect(host='localhost', user='root', password='Root123@@', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        
        #get the pymysql cursor
        self.cursor = self.conect.cursor()
        
        
          
        
    def CreatMyDB(self):
        
        self.db = "CREATE DATABASE IF NOT EXISTS Off_data"
        self.cursor.execute(self.db)
       