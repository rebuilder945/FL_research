ls=input()
a=eval(ls(0))
b=eval(ls(3))
c=ls(2)
ls1=[a]
for i in range(c-1):
    d=a+i*b
    ls1.append(d)
print(list(ls1))
