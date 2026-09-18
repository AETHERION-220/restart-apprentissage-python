# Exemple 1 : récupération d'un fichier HTML local
# Le script cherche le fichier à côté de lui, quel que soit le dossier courant.
from pathlib import Path
from bs4 import BeautifulSoup

base_dir = Path(__file__).resolve().parent
index_path = base_dir / "index.html"

with open(index_path, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file.read(), "html.parser")

# Exemple 2 : récupérer le titre de la page
print("Titre de la page :", soup.title)

# Exemple 3 : récupérer le texte d'un titre h1
# on suppose qu'il y a : <h1 id="titre">Bienvenue sur notre site</h1>
# titre = soup.find(id="titre")
# print("Texte du titre :", titre.get_text())

# Exemple 4 : récupérer des liens
# liens = soup.find_all("a")
# for lien in liens:
#     print(lien.get("href"))

# Exemple 5 : transformation de données
prix = "20 €"
prix_net = prix.replace("€", "").strip()
print("Prix netto :", prix_net)

prix_dollar = float(prix_net) * 1.2
print("Prix en dollars :", prix_dollar)

# Exemple 6 : extraction de produits depuis HTML
produits = [
    {"nom": "T-shirt", "prix": "20 €", "description": "Un tee-shirt confortable."},
    {"nom": "Pantalon", "prix": "40 €", "description": "Un pantalon élégant."},
]

resultats = []

for produit in produits:
    prix = produit["prix"].replace("€", "").strip()
    prix_dollar = float(prix) * 1.2

    resultats.append({
        "nom": produit["nom"],
        "prix_euro": prix,
        "prix_dollar": prix_dollar,
        "description": produit["description"]
    })

print("Produits transformés :", resultats)

print("Fin du programme.")
