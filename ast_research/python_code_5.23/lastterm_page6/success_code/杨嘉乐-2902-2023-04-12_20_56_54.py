n=eval(input())
sum=0
m=1
for i in range(n):
    sum+=(n+(i+1))/n
    n=n+(i+1)
print('%.4f'%sum)
