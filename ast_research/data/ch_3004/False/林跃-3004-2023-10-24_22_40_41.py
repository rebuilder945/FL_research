def sushu(x):
    y=[]
    for i in x:
        if i>=2:
            for j in range(2,i):
                if i%j==0:
                    break
                else:
                    y.append(i)
    print(y)
lst=eval(input())
sushu(lst)
