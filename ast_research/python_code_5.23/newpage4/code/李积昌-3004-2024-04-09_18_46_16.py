from ast import Pass


def sushu(n):
    for i in range(2,int(math.sqrt(n))+2):
        if n % i == 0:
            return False
    return True
b=eval(input())
a=[]
import math
for n in b :
    if n=0 :
        pass
    elif n=1 :
        pass
    

    elif sushu(n) ==True :
        a.append(n)
print(a)
        
