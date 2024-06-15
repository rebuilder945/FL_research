ls=list(input())
a=ls[0]
b=eval(ls[1])
c=ls[2]
ls1=[a]
for i in range(b-1):
    d=a+i*c
    ls1.append(d)
print(list(ls1))
