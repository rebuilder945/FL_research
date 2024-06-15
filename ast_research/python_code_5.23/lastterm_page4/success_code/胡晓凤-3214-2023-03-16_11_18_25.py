def one(y):
    x=[]
    for i in range(len(y)):
        if i!=0:
            x.append(i)
    for i in range(len(y)):
        if i==0:
            x.append(i)
    print(x)
sums=eval(input())
one(sums)
