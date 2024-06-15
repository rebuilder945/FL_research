ls=eval(input())
n,m=eval(input())
ls=list(ls)
ls1=[]
ls2=[]
if n>len(ls):
    print("error")
else:
    for i in range(-len(ls),len(ls)):
        if i==n:
            ls1.append(ls[i])
ls1=ls1*m
s=str(ls+ls1)
print(s)
        


