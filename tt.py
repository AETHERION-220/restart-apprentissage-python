import csv
from pathlib import Path

base_dir = Path(__file__).resolve().parent
file = base_dir / "data.csv"

en_tete = ["titre", "description"]
listes_de_titres = ["Article 1", "Article 2"]
listes_de_descriptions = ["Description 1", "Description 2"]

with open(file, "w", encoding="utf-8", newline="") as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=",")
    writer.writerow(en_tete)

    for titre, description in zip(listes_de_titres, listes_de_descriptions):
        writer.writerow([titre, description])

print(f"Fichier CSV créé : {file}")