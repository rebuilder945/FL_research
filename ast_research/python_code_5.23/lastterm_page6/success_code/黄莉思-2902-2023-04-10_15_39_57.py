n=eval(input())
s=0
a=2
b=1
for i in range(n):
    s+=a/b
    a=(a+b)/a
print("%.4f"%s)
