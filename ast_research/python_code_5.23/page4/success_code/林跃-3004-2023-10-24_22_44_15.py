def sushu(x):
    y=[]
    for i in x:
        if i>=2:
            for j in range(2,i,1):
                if i%j==0:
                    continue
            else:
                y.append(i)
    print(y)
lst=eval(input())
sushu(lst)
