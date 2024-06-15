h=eval(input())
n=eval(input())
sum=h
for i in range(1,n):
    a=2*10*(0.5**i)
    sum+=a
print('%.2f'%sum)
