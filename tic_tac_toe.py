##### PARTIE 1 #####

# on cree un tableau de trois cases, qui contiennent toutes un tableau de trois cases, 
# initialisées avec la chaine de caractere "_"
grilleDeJeu = [["_","_","_"], ["_","_","_"], ["_","_","_"]]

# on affiche nos tableaux imbriques sous forme de grille
for i in range(0, 3):
    print(grilleDeJeu[i][0], grilleDeJeu[i][1], grilleDeJeu[i][2])

