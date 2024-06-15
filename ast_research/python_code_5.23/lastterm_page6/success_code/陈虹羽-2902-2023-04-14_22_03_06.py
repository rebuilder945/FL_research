def num(n):
    a=[1,1]
    c=0
    for i in range(n):
        b=a[-1]+a[-2]
        a.append(b)
    for i in range(n):
        c+=a[i+2]/a[i+1]
    return c
n=eval(input())
print("%.4f"%(num(n)))


