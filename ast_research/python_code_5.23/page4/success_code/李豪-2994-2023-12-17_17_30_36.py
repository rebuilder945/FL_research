a=input().split()
a=list(a)
n,m=map(int,input().split(','))
if n >len(a):
    print("error")
else:
    c=a[n]
    for x in range(m):
        a.append(c)
        print(a)

