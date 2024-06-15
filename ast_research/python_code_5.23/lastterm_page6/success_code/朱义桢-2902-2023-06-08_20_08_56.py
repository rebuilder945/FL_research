a=eval(input())
b=[1,2]
for i in range(a-1):
    b.append(b[-1]+b[-2])
c=[]
for i in range(a):
    c.append(b[i+1]/b[i])
print("%.4f"%sum(c))
