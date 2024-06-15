jz=input()
lt=jz.split(sep=" ")
si=input()
ls=si.split(sep=" ")
n=ls[0]
m=ls[1]
a=lt[n]
b=lt[m]
a=str(a)
b=str(b)
lt.pop(n)
lt.insert(n,b)
lt.pop(m)
lt.insert(m,a)
print(lt)

