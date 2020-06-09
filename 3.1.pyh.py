# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:53:53 2020

@author: roy
"""
#
def solution(x, y):
    x=int(x); y=int(y)
    
    if x>10**50 or y>10**50 or x<1 or y<1:
        return('impossible')
    target=((x,y))
    bomb=((1,1))
    bombs=[bomb]
    bombs2=set()
    i=0
    if bomb==target:
      return(str(i))
    while True:#target[0]>=list(bombs)[-1][0] and target[1]>=list(bombs)[-1][1]:
     # print("bombs: ",bombs)
      
      i+=1
      
      #print("i: ",i)

      for bomb in bombs:
        #process one
        bomb1_1=((bomb[0]+bomb[1],bomb[1]))
        #print("BOMB1: ",bomb1_1)
        bombs2.add(bomb1_1)
        #process two
        bomb1_2=((bomb[0],bomb[1]+bomb[0]))
        #print("BOMB2: ",bomb1_2)
        bombs2.add(bomb1_2)
       
        if (bomb1_1==target) or (bomb1_2==target):
          #print('POSSIBLE ', target, " ",i)
          return(str(i))
        if (i>target[0]+target[1])*500:
            return('impossible')
#        if bomb1_1[0]>target[0]:
#            if bomb1_1[1]>target[1]:
#                if bomb1_2[0]>target[0]:
#                     if bomb1_2[1]>target[1]:
#                         #print('IMPOSSIBLE')
#                         return('impossible')
#        
           
                
      bombs=bombs2
      bombs2=set()
      
    return('impossible')


def solution2(x, y):
    
    M=x
    F=y
    gen=0
    m, f = int(M), int(F)
    while True:
        
        
    #print ("Mach",m)
    #print("Facula", f)230
    #print("gem", gen)
        if m == 1 and f == 1:
            return str(gen)
        if m<1 or f<1 or m==f:
            return "impossible"
        else:
            if m > f:
                if m > 100*f:
                    gen += int(m/f)
                    m = m - (int(m/f)*f)
                    
                else:
                    m-=f
                    gen += 1
            else:
                if f > 100*m:
                    gen += int(f/m)
                    f = f - (int(f/m)*m)
                else:
                    f-=m
                    gen += 1
                    
                    


def solution(x,y):
    x,y=int(x),int(y)
    gen=0
    while True:
        if x==y and y==1:
            return(str(gen))

        if x<1 or y<1 or x>10**50 or y>10**50 or y==x:# or (y==1 and x>100) or (x==1 and y>100):
        
            return('impossible')

        if x>y:
            
            x-=y
        elif y>x:
            
            y-=x
        gen+=1




def solution(x,y):
    x,y=int(x),int(y)
    gen=0
    while True:
        if x==1 and y==1:
            return(str(gen))

        if x<1 or y<1 or x>10**50 or y>10**50 or y==x:
            return('impossible')

        if x>y:
            
            x-=y
        elif y>x:
            
            y-=x
        gen+=1

def solution3(x,y):
    x,y=int(x),int(y)
    gen=0
    while x>1 or y>1:
        # if x==1 and y==1:
        #     return(str(gen))

        if x<1 or y<1 or y==x:# or (x%2==0 and y%2==0) or x>10**50 or y>10**50:
        
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

