# Les conditions permettent de contrôler le déroulement du programme.
# Si une condition est vraie, on exécute un bloc de code.
# Sinon, on exécute un autre bloc.

# Exemple 1 : condition simple avec if / else
age = 18

if age >= 18:
    print("Tu es majeur.")
else:
    print("Tu es mineur.")

# Exemple 2 : plusieurs conditions avec elif
note = 14

if note >= 18:
    print("Excellent")
elif note >= 12:
    print("Bien")
elif note >= 8:
    print("Passable")
else:
    print("A revoir")

# Exemple 3 : conditions combinées avec and
age = 22
est_etudiant = True

if age >= 18 and est_etudiant:
    print("Tu es adulte et étudiant.")
else:
    print("Tu ne remplis pas les deux conditions.")

# Exemple 4 : conditions combinées avec or
if age < 18 or est_etudiant:
    print("Au moins une condition est vraie.")
else:
    print("Aucune condition n'est vraie.")

# Exemple 5 : condition inversée avec not
if not est_etudiant:
    print("Tu n'es pas étudiant.")
else:
    print("Tu es étudiant.")

# Exemple 6 : comparaisons
nombre = 10

if nombre == 10:
    print("Le nombre est égal à 10.")

if nombre != 5:
    print("Le nombre n'est pas égal à 5.")

if nombre > 8:
    print("Le nombre est supérieur à 8.")

# Exemple 7 : vérification de parité
nombre = 7

if nombre % 2 == 0:
    print("C'est un nombre pair.")
else:
    print("C'est un nombre impair.")

# Exemple 8 : calculatrice simple
nombre_1 = 12
nombre_2 = 4
operation = "+"

if operation == "+":
    resultat = nombre_1 + nombre_2
    print("Le résultat est :", resultat)
elif operation == "-":
    resultat = nombre_1 - nombre_2
    print("Le résultat est :", resultat)
elif operation == "*":
    resultat = nombre_1 * nombre_2
    print("Le résultat est :", resultat)
elif operation == "/":
    if nombre_2 != 0:
        resultat = nombre_1 / nombre_2
        print("Le résultat est :", resultat)
    else:
        print("Impossible de diviser par 0.")
else:
    print("Opération inconnue.")

# Exemple 9 : match case (Python 3.10+)
fruit = "pomme"

match fruit:
    case "pomme":
        print("J'aime les pommes.")
    case "banane":
        print("Les bananes sont bonnes.")
    case "orange":
        print("Les oranges sont riches en vitamine C.")
    case _:
        print("Fruit inconnu.")

# Exemple 10 : conditions sur des chaînes de caractères
pseudo = "Tsaph"

if pseudo == "Tsaph":
    print("Bienvenue Tsaph !")
else:
    print("Pseudo inconnu.")

# Remarque importante :
# L'indentation est très importante en Python.
# Le code qui appartient au if doit être décalé.
# Sinon, Python va générer une erreur.

if True:
    print("Ce message s'affiche car la condition est vraie.")

print("Fin du programme.")
