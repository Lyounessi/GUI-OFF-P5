import pymysql
from pymysql import cursors

# creat connection to the server
conect = pymysql.connect(host='localhost', user='root', password='Root123@@', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        
#get the pymysql cursor
cursor = conect.cursor()