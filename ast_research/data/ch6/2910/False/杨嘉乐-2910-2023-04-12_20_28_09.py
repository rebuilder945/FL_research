h=eval(input())
m=eval(input())
sum=h
for i in range(m):
    h/=2
    sum+=2*h
print('%.2f'%sum)
