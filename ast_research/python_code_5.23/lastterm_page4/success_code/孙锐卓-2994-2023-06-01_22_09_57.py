a=input().split(',')
a=list(map(int,a))
n,m=input().split(',')
n,m=int(n),int(m)
b=len(a)
c=a.copy()

if n>=b or n<=-b:
    print("error")
else:
    x=a[n]
    d=[x]*m
    e=a+d
    print(e)




















































