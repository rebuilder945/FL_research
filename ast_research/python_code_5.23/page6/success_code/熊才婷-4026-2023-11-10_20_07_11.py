n=eval(input())
a=1
b=2
sum=2/1
for i in range(n-1):
    a=b
    b=a+b
    c=b/a
    sum+=c
print("%.4f"%sum)
