n=eval(input())
a=2
y=1
tt=0
while  n>0:
    tt+=a/y
    m=y
    y=a
    a=a+m
    n-=1
print(format(tt,'.4f'))

