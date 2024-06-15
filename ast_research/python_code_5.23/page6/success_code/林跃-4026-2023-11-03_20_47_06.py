n=eval(input())
a=1
b=2
sum=0
for i in range(n):
    sum=sum+b/a
    a=b
    b=b+a
print("%.4f"%sum)
