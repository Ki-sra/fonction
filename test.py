max_min()
def permuter(index1, index2):
    t[index1], t[index2] = t[index2], t[index1] 

def oredrdec():
    for i in range(len(t) - 1):
        for j in range(len(t) - 1 - i):
            if t[j] < t[j + 1]:  
                permuter(t[j],t[j+1] )  

oredrdec()

print('Le tableau en ordre décroissant :', t)
