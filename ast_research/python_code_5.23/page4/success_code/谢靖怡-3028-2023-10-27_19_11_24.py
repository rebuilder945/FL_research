ls=input()
a=int(ls(0))
b=int(ls(2))
c=int(ls(1))
ls1=[a]
for i in range(c-1):
    d=a+i*b
    ls1.append(d)
print(ls1)
