def s(i):
    for x in range(100,a+1):
        n=str(x)[0]
        m=str(x)[1]
        l=str(x)[2]
        if x==int(m)**3+int(n)**3+int(l)**3:
            return 1
        else:
            return 0
a=eval(input())
for x in range(100,a+1):
    if s(x)==1:
        print(x)
    else:
        print("none")
    

    

        







