a=list(input())
n,m=list(input())
if n>len(a):
    print("error")
else:
    b=a[n-1]
    for i in range(m):
        a.append(b)
    print(a)
