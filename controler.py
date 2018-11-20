"""Imports Parts"""
import urllib.parse
import requests
import pymysql.cursors
import models
import views
import connect
from constant import PREFIX_URL

class ModelMy():
    """class to execute the models querys"""
    def __init__(self):
        #define the cursor of pymysql to manipulate datas
        self.cursor = connect.cursor
        # creating objects that are imported from models
        self.cat = models.Cat()
        self.prods = models.Products()
        self.favs = models.Favorits()
        self.my_base = models.MyBase()
        #Geting the api's link of a specific categorie mentionned "creat_url method"
        self.req = requests.get(self.Creat_url('saucissons'))
    def Creat_url(self, nom_categorie):
        """This method  creat the link of the api that is 
        filtred by the categories using python urllib"""
        suffixe_url_element = {
            'action' : 'process',
            'tagtype_0' : 'categories',
            'tag_contains_0' : 'contains',
            'tag_0' : nom_categorie,
            'page_size' : '20',
            'page' : '1',
            'json' : '1'
        }
        url = PREFIX_URL + urllib.parse.urlencode(suffixe_url_element)
        return url    
    def CreatMyClass(self):
        """method to creat tables in the
        database as python code"""
        #self.cat.creat()
        #self.prods.create()
        #self.favs.create()
        #connect.db.commit()
        pass
    def clean_tables(self):
        """method to delete tables from the DB"""
        #self.my_base.Cleanclass("favorits")
        pass
    def Get_Insert_products(self):
        """method to get products from the 
        api and insert them inthe table"""
        #define the variabl that convert the api requests value as json format
        my_req = self.req.json()
        #define the key products that have all the data indeed as content inside the json dict
        prods = my_req["products"]
        #getting the id form categories table, situeted in the models
        self.cursor.execute(self.prods.get_id)
        got = self.cursor.fetchall()
        api_product = []
        #loop to eskape the double products valus in the products table
        for i in range(20):
            found = False
            for elt in api_product:
                if prods[i]["product_name"] == elt["product_name"]:
                    found = True
            if found == 0:
                api_product.append(prods[i])
        print(len(api_product))
        print(api_product[0]["product_name"], api_product[0]["stores_tags"])
        """execute the query of insert from models and 
        insert all the specific data in the table products"""
        for i in range(len(api_product)):
            val = (api_product[i]["product_name"], 
                   int(got[0]["id"]), 
                   ''.join(api_product[i]["stores_tags"]), 
                   ''.join(api_product[i]["nutrition_grades_tags"]), 
                   ''.join(api_product[i]["ingredients_tags"]), 
                   api_product[i]["url"])
            self.cursor.execute(self.prods.insert_data, val)
            
        connect.db.commit()
class ViewMy():
    """Class for the Views"""
    def __init__(self):
        #define the cursor of pymysql to manipulate datas
        self.cursor = connect.cursor
        #Geting all classes indeed
        self.cat = models.Cat()
        self.prods = models.Products()
        self.app = views.MyApp()
        #self.app.win.mainloop()
        #creat a tuple of categories value to add in the comobox of the view
        self.cats_val = ()
    def GetData_ToCats(self):
        """This Method used to append data into the categorie's combobox in the view"""
        # execute the query of selecting all datas from the categories
        self.cursor.execute(self.cat.get_cats) 
        # geting the value of the query
        my_cats = self.cursor.fetchall() 
        # making a tuple having the cat_name's datas
        self.cats_val =(my_cats[0]["cat_name"], 
                        my_cats[1]["cat_name"], 
                        my_cats[2]["cat_name"], 
                        my_cats[3]["cat_name"]) 
         # insert the values of the tuple self.cats_val in the combobox of categories
        self.app.combo_cat['values'] = self.cats_val
    def RuMe(self):
        """method to run the application with a loop"""
        self.app.win.mainloop()
"""Model run and execution"""
#run_model = models.MyBase()
#run_model.CreatMyDB()
in_modelmy = ModelMy()
#in_modelmy.CreatMyClass()
#in_modelmy.Get_Insert_products()
#in_modelmy.clean_tables()
"""View class runs"""
in_viewmy = ViewMy()
in_viewmy.GetData_ToCats()
in_viewmy.RuMe()
