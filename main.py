import unUplet as u
import doublet as d
import triplet as t
import sort
import numpy as np
from math import comb

n=int(input("n="))
k=0
S=0

l= []
lu = u.unUplet(n)
lu = sort.sort(lu, n)

ld = d.doublet(n)
lt = t.triplet(n)

for loop in range(n):
    l.append(lt[k])

    for d in range(n-1):
        l.append(ld[d+k*(n-1)])

    for u in range((n-k-1)*(n-k-2)):
        l.append(lu[u+S])

    S += (n-k-1)*(n-k-2)
    k+=1


print("Pour n={}, il y a {} triominos".format(n, len(l)))
for t in range(len(l)):
    print(l[t])