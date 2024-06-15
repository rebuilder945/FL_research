a=list(map(int,eval(input())))
n,m=eval(input())
d=[]
if (n+1) <=len(a):
    for x in range(m):
        d.append(a[n])
    a=a+d
    print(a)
else:
    print("error")
