n=eval(input())
a=1
b=2
sum=0
for i in range(n):
    sum=sum+b/a
    x=a
    a=b
    b=b+x
print("%.4f"%sum)
