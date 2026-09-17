# Les listes permettent de stocker plusieurs éléments dans une seule variable.
ma_liste = ["voiture", 2, 5, "mrkmk"]

# Exemple de listes de voitures par catégorie
mes_voitures_hybrides = ["toyota", "bmw", "mercedes"]
mes_voitures_electriques = ["range rover", "tesla", "audi"]

# Accès à un élément de la liste par index
print(mes_voitures_electriques[0])

# Les méthodes de liste permettent d'ajouter, modifier ou supprimer des éléments
mes_amis = ["mark", "jean", "luc", "david"]

# Ajouter un élément avec append()
mes_amis.append("Andre")
print(mes_amis)

# Modifier un élément avec son index
mes_amis[0] = "mathieu"
print(mes_amis)

# Supprimer un élément avec remove()
mes_amis.remove("jean")
print(mes_amis)

# Supprimer un élément par son index avec del
# Ici, on supprime l'élément en position 2
# Attention : le nombre d'éléments diminue après la suppression

del mes_amis[2]
print(mes_amis)

# len() permet de connaître le nombre d'éléments dans une liste
print(len(mes_amis))

# Les tuples sont comme des listes, mais ils sont immuables
mes_amis_tuple = ("mark", "jean", "luc", "david")
mes_nouveaux_amis = ("Andre", "christoph")

# On peut concaténer deux tuples pour en créer un nouveau
ma_nouvelle_liste = mes_amis_tuple + mes_nouveaux_amis
print(ma_nouvelle_liste)
