# Exemple 1 : importer un module simple
# On suppose qu'il existe un fichier operations.py contenant :
# def addition(a, b):
#     return a + b
#
# def multiplication(a, b):
#     return a * b

from operations import addition, multiplication

# Utilisation des fonctions importées
print("Addition :", addition(3, 5))
print("Multiplication :", multiplication(8, 2))

# Exemple 2 : import d'un module complet
import math

print("Carré de 9 :", math.sqrt(9))
print("Valeur de pi :", math.pi)

# Exemple 3 : utilisation simple d'un package installé avec pip
# pip install requests
# import requests
# reponse = requests.get("https://api.github.com")
# print(reponse.status_code)

# Exemple 4 : package personnalisé
# structure attendue :
# mon_package/
#     __init__.py
#     mon_module.py
#
# import mon_package.mon_module
# print(mon_package.mon_module.ma_fonction())

# Exemple 5 : import direct d'une fonction spécifique
# from mon_package.mon_module import ma_fonction
# print(ma_fonction())

print("Fin du programme.")
