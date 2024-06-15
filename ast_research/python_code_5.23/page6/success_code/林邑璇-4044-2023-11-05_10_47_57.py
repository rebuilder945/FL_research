def shuixianhuashu(x):
    t=False
    for i in range(100,x+1):
        c=0
        x=str(x)
        for i in range(3):
            c+=int(x[i])
        if c==x:
            print(c)
            t=True
        else:
            pass
    if t==False:
        print("none")
x=eval(input())
shuixianhuashu(x)

    

