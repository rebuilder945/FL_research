a=2
b=1
sum=0
n=int(input())
for i in range(1,n+1):
    sum=sum+a/b
    temp=b
    b=a
    a=b+temp
print("%.4f"%sum)

