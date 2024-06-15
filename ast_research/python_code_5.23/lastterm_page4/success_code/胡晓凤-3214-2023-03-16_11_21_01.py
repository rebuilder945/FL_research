def one(y):
    x=[]
    for i in y:
        if i!=0:
            x.append(i)
    for i in y:
        if i==0:
            x.append(i)
    print(x)
sums=eval(input())
one(sums)
