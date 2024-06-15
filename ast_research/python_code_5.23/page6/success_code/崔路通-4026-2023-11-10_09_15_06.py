a=2
b=1
c=0
n=eval(input())
while n>0:
    y=a
    x=b
    c+=y/x
    a=a+b
    b=a-b
    n-=1
print("%.4f"%c)



