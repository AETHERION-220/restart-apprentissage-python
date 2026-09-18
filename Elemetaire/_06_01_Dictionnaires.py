start_up = {
    "ceo": "Tsaphnath Kahuta",
    "nom_de_la_start_up": "Innova",
    "slogan": "L'innovation n'est que le début"
}
print(start_up)

nouvelle_campagne = {
    "responsable_de_campagne": "Jeanne d'Arc",
    "nom_de_campagne": "Campagne : Nous aimons les chiens",
    "date_de_debut": "01/01/2020",
    "influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}

print(nouvelle_campagne)

mon_programme = {}
mon_nouveau_programme = dict()

print(mon_programme)
print(mon_nouveau_programme)

mon_programme["Lundi"] = "Planifier la semaine, aller à la fac et se reposer."
mon_programme["Mardi"] = "Noter les tâches importantes et créer le repository du projet."

print(mon_programme)
print(mon_nouveau_programme)

mon_programme["Lundi"] = "Planifier et se concentrer sur les tâches les plus importantes pendant la première heure, puis sur les tâches moins prioritaires pendant la seconde heure."
print(mon_programme)

del mon_programme["Lundi"]
print(mon_programme)

mon_programme.pop("Mardi")
mon_programme.pop("Mardi")

print(mon_programme)
