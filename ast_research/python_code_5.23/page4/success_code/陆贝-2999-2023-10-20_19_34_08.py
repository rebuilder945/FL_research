jz=input()
lt=jz.split(sep=" ")
sz=input()
ls=sz.split(sep=" ")
n=ls[0]
m=ls[1]
n=int(n)
m=int(m)
a=lt[n]
b=lt[m]
a=str(a)
b=str(b)
lt.pop(b)
lt.insert(n,b)
lt.pop(a)
lt.insert(m,a)
print(lt)

