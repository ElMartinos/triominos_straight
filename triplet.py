import numpy as np

def triplet(n):
    l= np.empty((1,3), dtype=int)

    a=1
    for loop in range(n):
        l= np.append(l, [[a, a, a]], axis=0)
        a+=1
    
    l= np.delete(l, 0, 0)

    return(l)