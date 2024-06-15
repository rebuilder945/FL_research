a=eval(input())
n1=0
if a>99:
    for x in range(100,a):
        for i in str(x):
            n1=int(i)**3+n1
        if n1==x:
            print(x)
        else:
            continue
    else:
        print("none")
else:
    print("none")

