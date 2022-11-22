myTable = [8, 15, 37, 1, 12]

##### PARTIE 1 #####

# on utilise une variable temporaire pour echanger la premiere et la deuxieme valeurs du tableau
variableTemporaire = 0

variableTemporaire = myTable[0]
myTable[0] = myTable[1]
myTable[1] = variableTemporaire

##### PARTIE 2 #####

# on arrete le parcours de tableau une iteration avant la fin 
# car on ne peut pas comparer la derniere valeur avec une valeur qui n'existe pas (fin du tableau)
for i in range(0, len(myTable)-1):

    # si la valeur i est superieure a la valeur de la case suivante, on permute les deux cases
    if(myTable[i] > myTable[i+1]):
        variableTemporaire = myTable[i]
        myTable[i] = myTable[i+1]
        myTable[i+1] = variableTemporaire

