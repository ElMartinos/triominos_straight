import numpy as np

def doublet(n):
    l= np.empty((1, 3), dtype=int)

    a=1
    while a <= n:
        c=1
        while c <= n:
            if c == a:
                c+=1
            else:
                l= np.append(l, [[a, a, c]], axis=0)
                c+=1
        a+=1

    l= np.delete(l, 0, 0)

    return(l)