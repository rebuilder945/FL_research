n=eval(input())
a=2
b=1
total=0
for i in range(1,n+1):
    total=total+a/b
    a,b=a+b,a
print("%.4f"%total)
