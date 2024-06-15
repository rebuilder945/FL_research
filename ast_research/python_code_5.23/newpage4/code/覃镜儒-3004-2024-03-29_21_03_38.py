del sushu(y)
    x=[]
    for i in y:
        if i>=2:
            for j in range(2,i):
                if i%j==0:
                    break
                else:
                    x.append(i)
    print(x)
a=eval(input)
sushu(a)
