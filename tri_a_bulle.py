myTable = [8, 15, 37, 1, 12]

##### PARTIE 1 #####

# on utilise une variable temporaire pour echanger la premiere et la deuxieme valeurs du tableau
variableTemporaire = 0

variableTemporaire = myTable[0]
myTable[0] = myTable[1]
myTable[1] = variableTemporaire

