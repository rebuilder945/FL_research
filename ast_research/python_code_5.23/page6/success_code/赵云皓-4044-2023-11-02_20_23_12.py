a=eval(input())
b=0
if a<=100:
    print("none")
else:
    for x in range(100,a+1):
        f=str(x)
        l=0 
        for i in f:
            e=int(i)
            l=e**3+l
        if l==x:
            print(x)
            b=b+1
    if b==0:
        print("none")
