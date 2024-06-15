a=1
b=1
c=0
sum1=0
n=eval(input())
for i in range(n):
    c=b
    b=a
    a=c+b
    sum1=sum1+a/b
print("%.4f"%sum1)
    



