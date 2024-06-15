a=list(input())
a.append(",")
c=a[0:-1:2]
i=list(input())
n=int(i[0])
m=int(i[2])
if n<=len(c):
    n=list(n)
    n=n*m
    c=c+n
    print(c)
else:
    print("error")
