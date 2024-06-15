a=list(input().split())
n,m=eval(input())
if n>len(a):
    print("error")
else:
    b=a[n-1]
    for i in range(m):
        a.append(b)
    print(a)
