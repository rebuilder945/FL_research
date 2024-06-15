n=eval(input())
a=1
b=2
for i in range(n):
    s=s+b/a
    c=b
    b=b+a
    a=c
print("%.4f"%s)
