n=eval(input())
a=0
b=1
sum=0
for x in range(n):
    b=b+1
    a=a+1
    sum+=b/a
print("%.4f"%(sum))
