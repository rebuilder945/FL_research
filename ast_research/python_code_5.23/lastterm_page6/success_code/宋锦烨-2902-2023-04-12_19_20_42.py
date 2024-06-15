sum=0
a=2
b=1
n=int(input())
for i in range(n):
    sum+=(a/b)
    b,a = a,a+b
print('%.4f'%sum)
