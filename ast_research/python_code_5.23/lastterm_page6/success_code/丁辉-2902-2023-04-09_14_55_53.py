n=eval(input())
a=[1,2]
b=[]
for i in range(n-1):
    a.append(sum(a[i:i+2]))
for x in range(n+1):
    b.append(a[x+1]/a[x])
c=sum(b)
print("%.4f"%c)
