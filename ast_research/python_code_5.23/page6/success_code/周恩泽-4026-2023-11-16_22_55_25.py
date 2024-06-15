n1=eval(input())
s=0
a=2
b=1
for x in range(n1):
    s=s+a/b
    a,b=a+b,a
print("%.4f"%s)



