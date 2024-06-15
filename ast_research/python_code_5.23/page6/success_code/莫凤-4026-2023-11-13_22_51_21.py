n=eval(input())
a=1
b=2
e=0
for x in range(n-1):
    c=b/a
    d=a+b
    a=b
    b=d
    e+=c
print("%.4f"%(e))
