# Exemple 1 : créer un fichier texte avec open()
with open("hello.txt", "w", encoding="utf-8") as fichier:
    fichier.write("Hello, world!")

# Exemple 2 : lire un fichier texte
with open("hello.txt", "r", encoding="utf-8") as fichier:
    print(fichier.read())

# Exemple 3 : lire un fichier CSV avec csv.reader()
import csv

csv_data = [
    ["nom", "metier", "couleur_preferee"],
    ["Jacob Smith", "Ingenieur en informatique", "Violet"],
    ["Nora Scheffer", "Strategiste numerique", "Bleu"],
]

with open("couleurs_preferees.csv", "w", newline="", encoding="utf-8") as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=',')
    writer.writerows(csv_data)

with open("couleurs_preferees.csv", "r", encoding="utf-8") as fichier_csv:
    reader = csv.reader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne)

# Exemple 4 : lire un fichier CSV avec DictReader()
with open("couleurs_preferees.csv", "r", encoding="utf-8") as fichier_csv:
    reader = csv.DictReader(fichier_csv, delimiter=',')
    for ligne in reader:
        print(ligne['nom'], "travaille en tant que", ligne['metier'], "et sa couleur preferee est", ligne['couleur_preferee'])

# Exemple 5 : écrire un nouveau fichier CSV
with open("data.csv", "w", newline="", encoding="utf-8") as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=',')
    writer.writerow(["titre", "description"])

    titres = ["Article 1", "Article 2"]
    descriptions = ["Description 1", "Description 2"]

    for titre, description in zip(titres, descriptions):
        writer.writerow([titre, description])

print("Fin du programme.")
