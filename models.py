"""Imports Parts"""
import pymysql.cursors
import json
import connect
from connect import cursor

"""Starting Classes"""

class MyBase():
    
    def __init__(self):
        self.db = "CREATE DATABASE IF NOT EXISTS Off_data"   
        self.cursor = connect.cursor
        
          
        
    def CreatMyDB(self):
        
        
        self.cursor.execute(self.db)
       