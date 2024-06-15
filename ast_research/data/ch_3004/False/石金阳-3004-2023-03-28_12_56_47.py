def sushu(y):
    x=[]
    for m in y:
        if m>=2:
            for j in range(2,m,1):
                if m%j==0:
                    break
                else:
                    x.append(m)
    print(x)
suns=eval(input())
sushu(suns)
