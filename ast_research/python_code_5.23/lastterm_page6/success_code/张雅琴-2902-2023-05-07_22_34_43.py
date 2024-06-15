n=eval(input())
a=[1,1]
for i in range(0,n):
    a.append(a[-1]+a[-2])
b=[a[x+1]/a[x] for x in range(1,n+1)]
c=sum(b)
print("%.4f"%c)


