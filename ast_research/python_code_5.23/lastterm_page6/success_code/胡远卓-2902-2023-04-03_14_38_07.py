n=eval(input())
res=0
x1,x2=1,2
for i in range(n):
    res+=x2/x1
    x1,x2=x2,x1+x2
print("%.4f"%res)
