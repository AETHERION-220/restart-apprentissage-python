# 1. Création du dictionnaire fruits 
fruits = {"pomme": "rouge", "banane": "jaune", "orange": "orange"} 
print(fruits)

# 2. Ajout de la clé "kiwi" 
fruits["kiwi"] = "vert"
print(fruits)

 # 3. Accès à la valeur correspondant à la clé "banane" 
couleur_banane = fruits["banane"] 
print(fruits)
# 4. Modification de la valeur associée à la clé "pomme" 
fruits["pomme"] = "vert" 
print(fruits)
# 5. Suppression de la clé "orange" 
del fruits["orange"] 

# 6. Affichage des clés restantes dans le dictionnaire
print(fruits.keys())

print(fruits["pomme"])
print(fruits)