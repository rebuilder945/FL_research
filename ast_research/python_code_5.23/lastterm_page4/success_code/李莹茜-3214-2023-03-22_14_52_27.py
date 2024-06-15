def w0(y):
    x=[]
    for i in y:
        if i!=0:
            x.append(i)
    for i in y:
        if i==0:
            x.append(i)
    print(x)
ls=eval(input())
w0(ls)
