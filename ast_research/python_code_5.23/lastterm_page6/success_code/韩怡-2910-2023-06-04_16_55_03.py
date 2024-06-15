a=eval(input())
b=eval(input())
c=a
if b==1:
    print("%.2f"%c)
else:
    for i in range(0,b-1):
        a=a*0.5
        b=a*2
        c=c+b
    print("%.2f"%c)
