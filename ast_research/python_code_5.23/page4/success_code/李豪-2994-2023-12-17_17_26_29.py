a=input().split()
a=list(a)
n,m=map(eval,input().split())
if n >len(a)-1:
    print("error")
else:
    c=a[n]
    for x in range(m):
        a.append(c)
        print(a)

