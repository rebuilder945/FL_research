ls=list(eval(input()))
n,m=eval(input())
if n>len(ls)-1 or n<len(ls)*(-1):
    print("error")
elif ls[n] in ls :
    ls1=[]
    ls1.append(ls[n])
    ls2=ls1*m
    print(ls+ls2)
else:
    print("error")


