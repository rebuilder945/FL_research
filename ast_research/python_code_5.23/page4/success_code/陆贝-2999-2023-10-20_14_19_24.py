jz=input()
m,n=eval(input())
lt=list(jz)
a=lt(n)
b=lt(m)
lt.pop(a)
lt.pop(b)
lt.insert(a,m)
lt.insert(b,n)
print(lt)


