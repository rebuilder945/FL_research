def sushu(y):
    x=[];
    for i in y:
        if i>=2:
            if i%2==0:
                    break;
            else:
                x.append(i);
    print(x);
sums=eval(input());
sushu(sums);

