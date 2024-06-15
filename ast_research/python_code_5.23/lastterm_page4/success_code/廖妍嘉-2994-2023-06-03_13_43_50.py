ls=list(map(int,input().split(",")))
n,m=eval(input())
ls2=[]
if n<len(ls):
    a=ls[n]
    del ls[n]
    ls2.append(a)
    ls3=ls2*m
    print(ls+ls3)
else:
    print("error")


        

            


        
