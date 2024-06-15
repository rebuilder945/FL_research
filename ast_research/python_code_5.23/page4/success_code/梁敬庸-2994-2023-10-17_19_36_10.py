a=eval(input())
n,m=eval(input())
if n <len(a):
    d=a[n]
    for i in range(m):
        a.append(d)
    del a[n]
else:
    print("error")        


