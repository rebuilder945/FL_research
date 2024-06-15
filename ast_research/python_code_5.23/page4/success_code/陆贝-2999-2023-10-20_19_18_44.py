jz=input()
lt=jz.split(sep=" ")
n,m=eval(input())
a=lt[n]
b=lt[m]
lt.pop(n)
lt.insert(n,b)
lt.pop(m)
lt.insert(m,a)
print(lt)

