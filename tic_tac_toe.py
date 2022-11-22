##### PARTIE 1 #####

# on cree un tableau de trois cases, qui contiennent toutes un tableau de trois cases, 
# initialisées avec les chaines de caractere correspondant aux indices des cases
grilleDeJeu = [["0","1","2"], ["3","4","5"], ["6","7","8"]]

# on affiche nos tableaux imbriques sous forme de grille
for i in range(0, 3):
    print(grilleDeJeu[i][0], grilleDeJeu[i][1], grilleDeJeu[i][2])



##### PARTIE 2 #####

# on cree une variable comptant le nombre de tours de jeu, initialisee a 1
nbToursDeJeu = 1
# on initialise la variable caseAJouer a 0, elle contiendra l'indice de la case a jouer
caseAJouer = 0
gameNotOver = True

# tant que le jeu n'est pas fini on demande a l'utilisateur de jouer
while (gameNotOver):
    print("Saisissez le numero de la case a jouer")
    caseAJouer = int(input())

    # lorsque le tour est impair, un X sera affiche, sinon ce sera un O
    if (nbToursDeJeu % 2 != 0):
        grilleDeJeu[int(caseAJouer/3)][int(caseAJouer%3)]= "X"
    else:
        grilleDeJeu[int(caseAJouer/3)][int(caseAJouer%3)]= "O"

    # on affiche la grille de jeu a la fin de chaque tour
    for i in range(0, 3):
        print(grilleDeJeu[i][0], grilleDeJeu[i][1], grilleDeJeu[i][2])

    nbToursDeJeu = nbToursDeJeu + 1
