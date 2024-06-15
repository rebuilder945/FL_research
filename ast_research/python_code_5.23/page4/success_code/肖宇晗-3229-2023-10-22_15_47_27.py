def one(y):
    x=[]
    for i in y:
        if y.count(i)==1:
            x.append(i)
    x.sort(reverse=False)
    if x==[]:
        print(False)
    else:
        l = ','.join(str(j) for j in x)
        print(l)
sums=eval(input())
one(sums)
