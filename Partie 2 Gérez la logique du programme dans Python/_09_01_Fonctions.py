# Les fonctions permettent de regrouper des tâches et de réutiliser du code.
# Elles rendent le programme plus propre, plus lisible et plus facile à maintenir.

# Exemple 1 : fonction sans paramètre

def afficher_message():
    print("Bonjour, comment ça va ?")

# Appel de la fonction
afficher_message()

# Exemple 2 : fonction avec paramètres

def afficher_nom_prenom(nom, prenom):
    print("Nom :", nom)
    print("Prénom :", prenom)

# Appel de la fonction avec des valeurs
afficher_nom_prenom("Dupont", "Jean")

# Exemple 3 : fonction avec valeur de retour

def calculer_somme(a, b):
    resultat = a + b
    return resultat

somme = calculer_somme(2, 3)
print("La somme est :", somme)

# Exemple 4 : fonction qui multiplie deux nombres

def multiplier(x, y):
    return x * y

resultat = multiplier(4, 5)
print("Le résultat est :", resultat)

# Exemple 5 : fonction qui calcule la moyenne d'une liste

def calculer_moyenne(notes):
    total = sum(notes)
    moyenne = total / len(notes)
    return moyenne

mes_notes = [12, 15, 18]
print("La moyenne est :", calculer_moyenne(mes_notes))

# Exemple 6 : fonction qui retourne plusieurs valeurs

def infos_personne():
    nom = "Tsaph"
    age = 24
    return nom, age

prenom, age = infos_personne()
print("Nom :", prenom)
print("Age :", age)

# Exemple 7 : fonction avec condition

def est_pair(nombre):
    if nombre % 2 == 0:
        return True
    return False

print("10 est pair ?", est_pair(10))
print("7 est pair ?", est_pair(7))

# Exemple 8 : fonction simple pour saluer

def saluer():
    print("Salut !")

saluer()

print("Fin du programme.")
