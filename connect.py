"""The connect module present the connection to the server and to te database aswell"""
import pymysql
from pymysql import cursors
from getpass import getpass

LOGIN = input('login')
PASSWORD = getpass('password')
DBNAME = input('database name')
# creat connection to the server
db = pymysql.connect(host='localhost', user= LOGIN, password= PASSWORD, db=DBNAME, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)        
#get the pymysql cursor
cursor = db.cursor()
