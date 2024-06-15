n=eval(input())
a=1
b=2
for x in range(n):
    sum=sum+b/a
    a,b=b,a+b
print("%.4f"%sum)
