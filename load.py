fichier = open("hello.txt", "w")
fichier.write("hello, World !")
fichier.close()

with open("file.txt") as fichier_2 :
    lignes = 0
    for ligne in fichier_2 and lignes in range(0 , 2 , 20) :
        fichier_2.write(lignes)
        
        print(ligne)