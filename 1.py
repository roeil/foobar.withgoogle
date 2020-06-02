def squares(n):
    L = [i*i for i in range(1,n+1)]
    return L

#print (squares(16))

L=squares(15324)

Z=[x<15324 for x in L]
L[sum([1 if x==True else 0 for x in Z])-1]