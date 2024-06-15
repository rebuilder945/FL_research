a=eval(input())
b=1
c=2
d=[]
m=[1,2]
n=[2,3]
for i in range(a):
    m.append(m[i]+m[i+1])
    n.append(n[i]+n[i+1])
for i in range(a):
    d.append(n[i]/m[i])
print("%.4f"%sum(d))

