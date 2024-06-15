h=int(input())
n=int(input())
sum=0
while n>0:
    sum+=h+0.5*h
    n-=1
    h=0.5*h
print('%.2f'%sum)
