def solution(x,y):
    x,y=int(x),int(y)
    gen=0
    while x>1 or y>1:

        if x<1 or y<1 or y==x:
        
            return('impossible')

        if x>y:
            gen+=int(x/y)
            x%=y
        elif y>x:
            gen+=int(y/x)
            y%=x
        
        if(x == 0 or y == 0):
             gen-=1
    if gen==0:
        gen='impossible'
    return(str(gen))
