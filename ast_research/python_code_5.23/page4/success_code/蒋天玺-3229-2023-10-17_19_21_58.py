def one(y):
    x=[];
    for i in y:
        if y.count(i)==1:
            x.append(i);
    x.sort(reverse=False);
    if x==[]:
        print(False);
    else:
        print(*x,sep=',');
sums=eval(input());
one(sums);

