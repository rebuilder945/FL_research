n=eval(input())
a=1
b=2
sum=0
for i in range(n+1):
    sum=sum+b/a
    a=b
    b=b+a
print(sum)
