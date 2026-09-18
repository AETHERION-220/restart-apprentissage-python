# Les erreurs font partie du développement.
# Le but n'est pas de les éviter totalement,
# mais de les comprendre et de les gérer correctement.

# Exemple 1 : SyntaxError
# Le code suivant est faux car il manque les deux-points :
# if True
#     print("Bonjour")

# Exemple 2 : bonne syntaxe
if True:
    print("Bonjour")

# Exemple 3 : NameError
# Cela arrive si on utilise une variable non déclarée.
# print(age)

# Exemple 4 : TypeError
# On ne peut pas additionner directement une chaîne et un nombre.
# print(5 + "bonjour")

# Exemple 5 : IndexError
ma_liste = [1, 2, 3]
# print(ma_liste[10])

# Exemple 6 : KeyError
mon_dictionnaire = {"nom": "Tsaph"}
# print(mon_dictionnaire["age"])

# Exemple 7 : ValueError
# int("bonjour")

# Exemple 8 : gestion des erreurs avec try/except
while True:
    try:
        nombre = int(input("Entrez un nombre entier : "))
        print("Votre nombre est :", nombre)
        break
    except ValueError:
        print("Erreur : veuillez entrer un nombre entier.")

# Exemple 9 : gestion de la division par zéro
try:
    resultat = 10 / 0
except ZeroDivisionError:
    print("Erreur : division par zéro impossible.")

# Exemple 10 : docstring et fonction propre

def somme(a, b):
    """
    Cette fonction calcule la somme de deux nombres.

    Paramètres :
    a (int): premier nombre
    b (int): deuxième nombre

    Retourne :
    int: la somme de a et b
    """
    return a + b

print("La somme est :", somme(5, 8))

# Exemple 11 : DRY (ne pas se répéter)

def ajouter_dix(nombre):
    return nombre + 10

print(ajouter_dix(10))
print(ajouter_dix(20))
print(ajouter_dix(30))

# Exemple 12 : code lisible et code peu lisible
prix_total = 15
TVA = 0.20
prix_ttc = prix_total + (prix_total * TVA)
print("Prix TTC :", prix_ttc)

# Les bonnes pratiques :
# - utiliser des noms de variables clairs
# - éviter le copier-coller inutile
# - séparer les tâches en fonctions
# - commenter les parties importantes
# - respecter l'indentation
# - gérer les exceptions lorsqu'il le faut

print("Fin du programme.")
