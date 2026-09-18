# Les boucles permettent de répéter des actions.
# Elles sont très utiles pour parcourir des listes, des chaînes, ou exécuter un code tant qu'une condition est vraie.

# Exemple 1 : boucle for sur une liste
races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]

for chien in races_de_chien:
    print(chien)

# Exemple 2 : boucle for sur une chaîne de caractères
mot = "Python"

for lettre in mot:
    print(lettre)

# Exemple 3 : boucle for avec range()
for x in range(5):
    print(x)

# Exemple 4 : boucle for avec formatage de texte
for x in range(5):
    print(f"{x} bouteilles de bière au mur !")

# Exemple 5 : boucle for avec un autre intervalle
for x in range(4, 10):
    print(x)

# Exemple 6 : boucle while
capacite_actuelle = 3
capacite_maximale = 10

while capacite_actuelle < capacite_maximale:
    capacite_actuelle += 1
    print(capacite_actuelle)

# Exemple 7 : boucle infinie à éviter
# x = 0
# while x != 5:
#     x += 2
# Cette boucle ne s'arrête jamais, car x n'atteint jamais 5.

# Exemple 8 : break
for i in range(10):
    if i == 5:
        break
    print(i)

# Exemple 9 : continue
for element in [1, 2, 3, 4, 5]:
    if element == 3:
        continue
    print(element)

# Exemple 10 : boucle pour multiplier chaque élément d'une liste
nombres = [1, 2, 3, 4, 5]

for nombre in nombres:
    print(nombre * 2)

# Exemple 11 : boucle for avec condition interne
mot = "bonjour"

for lettre in mot:
    if lettre == "o":
        print("J'ai trouvé la lettre o")

# Exemple 12 : comparaison entre for et while
# for : on sait exactement le nombre d'itérations
for i in range(5):
    print(i)

# while : on continue tant que la condition reste vraie
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1

print("Fin du programme.")
