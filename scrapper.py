import csv
from pathlib import Path

base_dir = Path(__file__).resolve().parent
file_path = base_dir / "couleur_preferree.csv"

with open(file_path, "r", encoding="utf-8", newline="") as fichier_csv:
    reader = csv.reader(fichier_csv, delimiter=",")
    for ligne in reader:
        print(ligne)
