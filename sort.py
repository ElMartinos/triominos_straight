import numpy as np

def sort(l, n):
    arr = np.empty((1, 3), dtype= int)
    k= 0
    repet= 0

    while (n-k-2)*(n-k-1)>0:
        k+=1
        
    pair=[]
    for e in range(k+1):
        pair.append(2*e)

    S=-1
    i=0
    
    for loop in range(k):
        S += (n-i-1)*(n-i-2)

        j = k-1
        S_ins = 0
        for loop in range(k-i):
            decalage = 0
            
            for loop in range(k-j):
                arr = np.append(arr, [l[S - S_ins - 1 + pair[decalage],:]], axis=0)
                arr = np.append(arr, [l[S - S_ins + pair[decalage],:]], axis=0)
                decalage+=1

            j-=1
            S_ins += 2*(k-j)

        i+=1

    arr=np.delete(arr, 0, 0)
    return(arr)