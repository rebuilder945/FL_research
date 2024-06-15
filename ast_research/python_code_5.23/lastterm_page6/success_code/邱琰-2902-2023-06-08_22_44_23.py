n=eval(input())
a=[2,3]
b=[1,2]
for i in range(1,n-1):
    a.append(a[i-1]+a[i])
    b.append(b[i-1]+b[i])
s=0
for i in range(n):
    s+=a[i]/b[i]
print("%.4f"%(s))
