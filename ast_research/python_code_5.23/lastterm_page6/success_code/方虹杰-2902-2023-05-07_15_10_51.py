n=eval(input())
a=2
b=1
c=[]
for i in range(n):
    s=a/b
    c.append(s)
    a,b=a+b,a
print("%.4f"%(sum(c)))
