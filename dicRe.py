import csv
from pathlib import Path

base_dir = Path(__file__).resolve().parent
file_path = base_dir / "couleur_preferree.csv"

with open(file_path, "r", encoding="utf-8", newline="") as file_csv:
    reader = csv.DictReader(file_csv, delimiter=",")
    for ligne in reader:
        print(f"{ligne['nom']} travaille en tant que {ligne['metier']} et sa couleur préférée est {ligne['couleur_preferee']}")

