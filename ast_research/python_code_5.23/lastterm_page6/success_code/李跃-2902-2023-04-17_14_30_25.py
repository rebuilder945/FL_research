n=eval(input())
a=1
b=2
c=0
c=c+b/a
a=a+1
d=b
b=3
for x in range (n-1):
    c=c+b/a
    a=a+1
    b=b+d
print("%.4f"%(c))
