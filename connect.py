import pymysql
from pymysql import cursors

# creat connection to the server

db = pymysql.connect(host='localhost', user='root', password='Root123@@', db='off_data', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)        
#get the pymysql cursor
cursor = db.cursor()
