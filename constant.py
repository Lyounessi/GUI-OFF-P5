import urllib.parse

"""Here Is All constant indeed in the project"""

"""TABLES"""

T_CAT = "categories"
T_PRODS = "products"
T_FAV = "favorits"

"""API URLS"""
url = "https://fr.openfoodfacts.org/cgi/search.pl"
url_fix={
    
    'action':'process',
    'tagtype_0':'categories',
    'tag_contains_0':'contains',
    'tag_0':'',
    'page_size':'20',
    'page':'1',
    'json':'1',
}
print(url + urllib.parse.urlencode(url_fix))

