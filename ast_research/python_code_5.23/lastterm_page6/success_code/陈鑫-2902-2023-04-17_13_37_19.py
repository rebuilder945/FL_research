n=eval(input())
a=[1,2]
c=[]
for i in range(n):
    b=a[-1]+a[-2]
    a.append(b)

for i in range(n):
    d=a[i+1]/a[i]
    c.append(d)

e=sum(c)
print("%.4f"%e)
    


