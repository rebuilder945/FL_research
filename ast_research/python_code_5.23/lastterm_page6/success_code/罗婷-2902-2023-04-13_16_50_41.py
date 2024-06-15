n=eval(input())
x=0
m=2
z=3
middle=0
su_m=0
for i in range(1,n+1):
    middle=m
    m=z
    z+=middle
    su_m+=middle/i
print('%.4f'%su_m)
