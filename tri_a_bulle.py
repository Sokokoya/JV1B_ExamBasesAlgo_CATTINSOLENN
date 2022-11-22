##### PARTIE 1 #####

myTable = [8, 15, 37, 1, 12]

# on utilise une variable temporaire pour echanger la premiere et la deuxieme valeurs du tableau
variableTemporaire = 0

variableTemporaire = myTable[0]
myTable[0] = myTable[1]
myTable[1] = variableTemporaire



##### PARTIE 2 #####

myTable = [8, 15, 37, 1, 12]

# on arrete le parcours de tableau une iteration avant la fin 
# car on ne peut pas comparer la derniere valeur avec une valeur qui n'existe pas (fin du tableau)
for i in range(0, len(myTable)-1):

    # si la valeur i est superieure a la valeur de la case suivante, on permute les deux cases
    if(myTable[i] > myTable[i+1]):
        variableTemporaire = myTable[i]
        myTable[i] = myTable[i+1]
        myTable[i+1] = variableTemporaire



##### PARTIE 3 #####

myTable = [8, 15, 37, 1, 12]
print(myTable)

for i in range(0, len(myTable)):
    # on ne compare les valeurs que dans ce qui n'a pas ete change
    # on parcours donc le tableau de 0 a la taille du tableau auquel on a retire les valeurs 
    # deja triees (donc i)
    for j in range(0, len(myTable)-(1+i)):

        if(myTable[j] > myTable[j+1]):
            variableTemporaire = myTable[j]
            myTable[j] = myTable[j+1]
            myTable[j+1] = variableTemporaire

# on ecrit a l'ecran le tableau bien trie
print(myTable)



##### PARTIE 4 #####

"""Le tri a bulle est lent car on y retrouve deux boucles pour imbriquées
dans ces boucles on a en plus une verification de condition ce qui a egalement un cout temporel
non negligeable sur des tableaux de taille tres grande
L'ordre de grandeur du temps necessaire a son execution est de n², n etant le nombre de tours de tableau
(donc la taille du tableau)"""



