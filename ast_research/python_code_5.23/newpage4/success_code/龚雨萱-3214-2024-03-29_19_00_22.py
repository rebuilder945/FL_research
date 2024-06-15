ls=eval(input())
a=[]
n=ls.count(0)
b=[0]*n
for i in ls:
    if i !=0:
        a.append(i)
c=a+b
print(c)
