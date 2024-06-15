def P(x):
    for i in range(2,x+1):
            for j in range(2,i):
                if i%j==0:
                    return False
                
                return True
x=eval(input())
i=2
t=0
while t<x:
     if str(i)==str(i)[::-1] and P(x):
          print(i,end=' ')
          t+=1
     i+=1
