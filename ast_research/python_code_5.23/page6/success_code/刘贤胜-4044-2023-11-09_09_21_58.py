a=eval(input())
n2=0
if a>99:
    for x in range(100,a+1):
        n1=0
        for i in str(x):
            n1=int(i)**3+n1
        if n1==x:
            print(x)
            n2=n2+1
        else:
            continue
    if n2==0:
        print("none")
else:
    print("none")

