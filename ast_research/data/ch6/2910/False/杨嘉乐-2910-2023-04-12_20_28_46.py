h=eval(input())
m=eval(input())
sum=h
for i in range(m):
    sum+=h
    h/=2
print('%.2f'%sum)
