n=0
lstx=[]
def solution(area):
    
    def squares(n):
        L = [i*i for i in range(1,n+1)]
        return L

        
    if area==0:
        return lstx
    
    
    elif (area ** 0.5).is_integer():
        lstx.append(area)
        return(lstx)
    
    else:
    
        L=squares(area)
    
        Z=[x<area for x in L]
        n=L[sum([1 if x==True else 0 for x in Z])-1]
        #print(n)
        lstx.append(n)
        return(solution(area-n))
#    else:
#        return None
    