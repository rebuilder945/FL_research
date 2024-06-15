n=int(input())
sum=0
a=1
b=2
for i in range (n):
    sum+=b/a
    a,b=b,a+b
print("%.4f"%sum)
