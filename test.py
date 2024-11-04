max_min()
def permuter(index1, index2):
    t[index1], t[index2] = t[index2], t[index1] 

def oredrdec():
    for i in range(len(t) - 1):
        for j in range(len(t) - 1 - i):
            if t[j] < t[j + 1]:  # Si l'élément courant est inférieur au suivant
                permuter(t[j],t[j+1] )  # Utiliser la fonction permuter pour échanger les éléments

oredrdec()

print('Le tableau en ordre décroissant :', t)
