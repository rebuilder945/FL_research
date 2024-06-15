n=eval(input())
m=[]
a=1
b=2
for i in range(n):
    m.append(b/a)
    x=b
    b=b+a
    a=x
c=sum(m)
print("%.4f"%c)
