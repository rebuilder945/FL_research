ls=list(eval(input()))
n,m=eval(input())
ls1=[]
if n in range(0,len(ls)):
    ls1.append(ls[n])
    ls2=ls1*m
    print(ls+ls2)
elif n in range(-len(ls),0):
    ls1.append(ls[n])
    ls2=ls1*m
    print(ls+ls2)
else:
    print("error")
