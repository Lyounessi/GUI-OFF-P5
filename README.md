# OPENFOODFACTS desktop application (an OC project)

This project is a part of the path python applications developer, in the OC educational platform.

# Getting Started
Before using the application, make sure you have instaled the requirements.
1- cd to the directory where requirements.txt is located.
2- activate your virtualenv.
3- run: pip install -r requirements.txt in your shell

# Built With
- python 3.7.0
- tkinter
- mysql

# PS DATABASE

No script avaible for the database, cause it was made by methods inside the file models.py

# MVC's files

- controler.py :
    This file present the controler as interaction between the view and the models, to execute every methods and querys existing in the other files.
- views.py : 
    This file present the GUI code, design and structur of the GUI for a beter User experience.
- models.py :
    In this file we find all class representing the tables inside the database, also all queries and methods for selections insertions .. etc
- connect.py : 
    Making the connexion to the database and the server which in this case is located in the localhost.
- constant.py : 
    This file is not yet completed to make all constants indeed.
- logo.ico :
    an image represent the logo of the application

# Author

Boukroun Younes