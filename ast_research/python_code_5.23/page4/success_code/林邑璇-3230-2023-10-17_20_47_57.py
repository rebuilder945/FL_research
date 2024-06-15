a=eval(input())
b=len(a)
e=0
for i in range(b):
    c=max(a)
    d=len(a)
    a.remove(c)
    e=e+c*10**(d-1)
print(e)

