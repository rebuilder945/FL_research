n=eval(input())
a=2
b=1
sum=0
for i in range(n):
     sum=sum+a/b
     b,a=a,a+b
print("%.4f"%sum)
