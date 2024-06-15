a=eval(input())
n,m=eval(input())
c=len(a)
if n>c or m>c+2:
    print('error')
elif n>m:
    print('error')
else:
    for i in a[0,n]:
        a.append(i)
    for i in a[m,c]:
        a.append(i)
    print(a)
