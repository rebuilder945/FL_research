n=eval(input())
a=1
b=2
sum=0
for i in range(n):
    c=b/a
    a,b=b,a+b
    sum+=c
print("%.4f"%sum)

