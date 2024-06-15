a=list(input())
a.append(",")
c=a[0:-1:2]
n,m=int(input())
if n<=len(c):
    n=list(n)
    n=n*m
    c=c+n
    print(c)
else:
    print("error")
