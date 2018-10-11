"""Here Is All constant indeed in the project"""

"""TABLES"""

T_CAT = "categories"
T_PRODS = "products"
T_FAV = "favorits"

"""API URLS"""

BOISSON_URL = "https://fr.openfoodfacts.org/magasin/super-u/categorie/boissons.json"
FROMAGE_URL = "https://fr.openfoodfacts.org/categorie/fromages.json"
PROD_TARTINER_URL = "https://fr.openfoodfacts.org/categorie/charcuteries.json"
CHARCUTERIE_URL = "https://fr.openfoodfacts.org/categorie/produits-a-tartiner.json"

"""API QUERYS"""
INSERT= "INSERT INTO products VALUES (%s, %s, %s, %s, %s)"
