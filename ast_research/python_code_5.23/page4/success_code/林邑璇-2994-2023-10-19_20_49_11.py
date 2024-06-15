
a=list(map(int,input().split(",")))
n,m=eval(input())
b=len(a)
if n>b-1:
    print("error")
else:
    c=a[n]
    for i in range(m):
        a.append(c)
    print(a)


