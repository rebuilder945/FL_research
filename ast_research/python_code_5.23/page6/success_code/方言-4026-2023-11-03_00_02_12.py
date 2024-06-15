a=1
b=2
n=int(input())
sum=b/a
for i in range(n-1):
    b=b+a;a=b-a
    sum+=b/a
print("%.4f"%sum)
