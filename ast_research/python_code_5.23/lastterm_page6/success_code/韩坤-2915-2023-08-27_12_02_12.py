a=eval(input())
if a<=100:
    print("none")
elif 100<a<=1000:
    for i in range(100,a+1):
        b=list(str(i))
        b1=int(b[0])
        b2=int(b[1])
        b3=int(b[2])
        if i==(b1)**3+(b2)**3+(b3)**3:
            print(i)
        else:
            pass
else:
    for i in range(100,1001):
        b=list(str(i))
        b1=int(b[0])
        b2=int(b[1])
        b3=int(b[2])
        if i==(b1)**3+(b2)**3+(b3)**3:
            print(i)
        else:
            pass
