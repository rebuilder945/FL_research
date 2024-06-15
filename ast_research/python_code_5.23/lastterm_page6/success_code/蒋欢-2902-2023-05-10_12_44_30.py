n=eval(input())
x=2
y=1
sum=0
for i in range(n):
    sum+=x/y
    m=y
    y=x
    x=x+m
print("%.4f"%sum)
