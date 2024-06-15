def sushu(y)
    a=[]
    for i in y:
        if i>=2:
            for m in range(2,i,1):
                if i%m==0:
                    break
                 else:
                     a.append(i)
sums=eval(input())
sushu(sums)

