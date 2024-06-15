a=input()
ls1=a.split(",")
ls2=eval(input())
ls=[]
ls3=[]
for i in range(len(ls1)):
    m=ls1[i]
    n=ls2[i]
    a=[m,n]
    ls3.append(a)
print(ls3)

