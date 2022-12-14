##### PARTIE 1 #####

# on cree un tableau de trois cases, qui contiennent toutes un tableau de trois cases, 
# toutes initialisées avec une chaine de caractere correspondant a leur indice
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


    ##### PARTIE 3 #####

    # on verifie si un joueur a gagné en diagonale
    # si c'est le cas, le jeu est fini et on affiche un message de victoire
    if ((grilleDeJeu[0][0] == grilleDeJeu[1][1]) and (grilleDeJeu[0][0] == grilleDeJeu[2][2])):
        gameNotOver = False
        print("Bravo ! le joueur", (nbToursDeJeu+1)%2+1, "a gagne !")

    elif ((grilleDeJeu[0][2] == grilleDeJeu[1][1]) and (grilleDeJeu[0][2] == grilleDeJeu [2][0])):
        gameNotOver = False
        print("Bravo ! le joueur", (nbToursDeJeu+1)%2+1, "a gagne !")


    # on verifie si un joueur a gagné en ligne
    # si c'est le cas, le jeu est fini et on affiche un message de victoire
    for i in range(0, 3):
        # verification sur les lignes verticales
        if ((grilleDeJeu[0][i] == grilleDeJeu[1][i]) and (grilleDeJeu[i][i] == grilleDeJeu[2][i])):
            gameNotOver = False
            print("Bravo ! le joueur", (nbToursDeJeu+1)%2+1, "a gagne !")
            break

        # verification sur les lignes horizontales
        elif ((grilleDeJeu[i][0] == grilleDeJeu[i][1]) and (grilleDeJeu[i][i] == grilleDeJeu[i][2])):
            gameNotOver = False
            print("Bravo ! le joueur", (nbToursDeJeu+1)%2+1, "a gagne !")
            break


    ##### PARTIE 4 #####

    # on verifie si le nombre de tour est egal a neuf (nombre de cases dans la grille)
    # si oui, le jeu est fini, si non, on passe au tour suivant en incrementant la 
    # variable nbToursDeJeu
    if (nbToursDeJeu == 9):
        gameNotOver = False
    else:
        nbToursDeJeu = nbToursDeJeu + 1


##### PARTIE 6 #####

"""Pour programmer un jeu de Puissance 4 il faudra :
    - Changer la taille de la grille pour une grille 7x6
    - Changer la condition de victoire du jeu : il faut que 4 jetons de la meme couleur soient consecutifs
    - Peut etre utiliser des couleurs
    - la partie n'est plus finie lorsque 9 tours ont passé, mais lorsque 42 tours (7*6 tours) ont été joués
Les regles restent sinon globalement les memes :
    - Chaque joueur pose un pion a son tour
    - Lorsque 4 sont alignés, en ligne, colonne ou diagonale, le jeu s'arrete
"""