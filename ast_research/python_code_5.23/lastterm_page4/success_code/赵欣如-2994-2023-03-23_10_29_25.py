ls=list(eval(input()))
n,m=eval(input())
if ls.index(n) not in ls :
    print("error")
else:
    ls1=[]
    ls1.append(ls[n])
    ls2=ls1*m
    print(ls+ls2)


