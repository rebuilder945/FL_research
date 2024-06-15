a=eval(input())
n,m=eval(input())
if n in range(a):
    d=a[n]
    for i in range(m):
        a.append(d)
    del a[n]
else:
    print("error")        


