def w0(y):
    x=[]
    for i in y:
        if i!=0:
            x.append(i)
    for i in y:
        if i==0:
            x.append(i)
ls=eval(input())
print(w0(ls))
