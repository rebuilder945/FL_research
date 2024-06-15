x=1
y=2
n = eval(input())
s = 0
while n>0:
    s = y/x +s
    m = x
    x=y
    y=m+y
    n-=1
print('%.4f'%s)


