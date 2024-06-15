A1=list('abcdefghijklmnopqrstuvwxyz')
A=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
a=A1+A
B1=A1.copy()
B=A.copy()
B1.reverse()
B.reverse()
b=B1+B
c={}
for i in range(len(a)):
    c[a[i]]=b[i]
n=input()
m=list(n)
for r in m:
    if r in a:
        print(c[r],end='')
    else:
        print(r,end="")
print('')
print(n)

