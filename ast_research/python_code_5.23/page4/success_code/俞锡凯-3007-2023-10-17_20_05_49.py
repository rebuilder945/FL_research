a=eval(input())
n,m=eval(input())
c=len(a)
if n>c or m>c+2:
    print('error')
elif n>m:
    print('error')
else:
    a.pop(n,m)
    print(a)
