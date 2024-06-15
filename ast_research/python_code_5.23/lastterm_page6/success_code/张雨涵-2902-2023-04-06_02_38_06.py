n = eval(input())
d=[1,1]
a=[]
for i in range(n):
    s = d[i]+d[i+1]
    d.append(s)
    t = d[i+2]/d[i+1]
    a.append(t)
print("%.4f"%sum(a))
