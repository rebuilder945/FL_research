n=eval(input())
a=1
b=2
sum=2/1
for i in range(n-1):
    m=b
    b=a+b
    c=b/a    
    sum+=c
    a=m
print("%.4f"%sum)
