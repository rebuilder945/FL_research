n=eval(input())
b=2
a=1
c=[]
for i in range(1,n+1):
    c.append(b/a)
    b,a=b+a,b
    
print("%.4f"%(sum(c)))
