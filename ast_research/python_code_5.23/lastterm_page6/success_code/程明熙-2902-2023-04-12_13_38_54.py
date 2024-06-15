from re import A


n=eval(input())
a=2
b=1
t=0
for i in range(0,n):
    t+=(a)/(b)
    a,b=a+b,a
print('%.4f'%t)


# 2/1,3/2,5/3,8/5,13,21
