a=eval(input())
c=list(map(int,a))
n,m=eval(input())
if n>len(c):
    print("error")
else:
    b=c[n-1]
    for i in range(m):
        c.append(b)
    print(c)
