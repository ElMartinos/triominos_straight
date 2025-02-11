import numpy as np

def unUplet(n):
    l= np.empty((1, 3), dtype=int)
    k = 0

    while ((n-k-1)*(n-k-2))/2 > 0:
        a = k+1
        b = 1
        while b < n:
            if b == a:
                b+=1
            else:
                c = b+1
                while c <= n:
                    if c == a:
                        c+=1
                    else:
                        if a<k+1 or b<k+1 or c<k+1:
                            c+=1

                        else:
                            l= np.append(l, [[a, b, c]], axis=0)
                            l= np.append(l, [[a, c, b]], axis=0)
                            c+=1
                b+=1
        k+=1

    l= np.delete(l, 0, 0)

    return(l)