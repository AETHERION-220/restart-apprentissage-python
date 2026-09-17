#print("I'm learning python")
#print(17+35*2)

#livre = "Gatsby le Magnifique"

# nom = "tsaphnath"
# age = 19
# taille = 1,69
# est_etudiant = True

# print(f"Bonjour {nom}, c'est exellent que tu puisse avoir {age} ans et mesurer {taille}. A ce que je vois tu es encore etudiant ? {est_etudiant} ")

# print(type(nom))
# print(type(age))
# print(type(taille))
# print(type(est_etudiant))

#liste

plateformes_sociales = ["Facebook", "Instagram", "Twitter", "Snapchat"]

print(plateformes_sociales[0])
print(plateformes_sociales[1])
print(plateformes_sociales[2]) 
language = "PYTHON"
print(language[0])
print(language[1])
print(language[2])
print(language[3])

print(language[-4])

plateformes_sociales[2] = "LinkedIn"
print(plateformes_sociales)
plateformes_sociales.append("Tiktok")

print(plateformes_sociales)

plateformes_sociales.remove("Snapchat")
print(plateformes_sociales)

print(len(plateformes_sociales[2]))


ma_liste = []
print(ma_liste)

ma_liste = ["a", "b", "c", "d"]
print(ma_liste)

print(ma_liste[2])

ma_liste[2] = "z"
print(ma_liste)

ma_liste.append("e")
print(ma_liste)

ma_liste.remove("z")
print(ma_liste)

del ma_liste[0]

print(ma_liste)

ma_chaine = "Hello, world"

print(ma_chaine[0])

mon_tuple = (1, 2, 3, 4)
print(mon_tuple)
print(mon_tuple[2])

mon_tuple_bis = ("cinq", "six")

mon_nouveau_tuple = mon_tuple + mon_tuple_bis

print(mon_nouveau_tuple)

nombres = [1,2,3,4,5]

print(5 in nombres)
print(8 in nombres)

fruits = ["pomme", "banane", "orange"]
fruits.append("kiwi")
print(fruits)

# fruits.remove("orange")
print(fruits)

del fruits[2]
print(fruits)

fruits[2]= "ananas"
print(fruits)

print(len(fruits))

fruits.sort()

print(fruits)

mes_amis = ("mark", "jean" , "luc", "david")

print(mes_amis[0])



print(mes_amis)

mes_amis.sort()
