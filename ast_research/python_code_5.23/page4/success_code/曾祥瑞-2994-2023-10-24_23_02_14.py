a=input()
c=list(map(int,a.split()))
n,m=eval(input())
if n>len(c):
    print("error")
else:
    b=c[n-1]
    for i in range(m):
        c.append(b)
    print(c)
