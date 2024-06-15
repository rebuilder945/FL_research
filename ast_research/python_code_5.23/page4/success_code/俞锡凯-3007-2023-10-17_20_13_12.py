a=eval(input())
n,m=eval(input())
c=len(a)
b=[]
if n>c or m>c+2:
    print('error')
elif n>m:
    print('error')
else:
    for i in range(0,n):
        b.append(a[i])
    for i in range(m,c):
        b.append(a[i])
    print(a)
