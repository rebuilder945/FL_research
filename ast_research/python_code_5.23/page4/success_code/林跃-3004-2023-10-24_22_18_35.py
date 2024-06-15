def sushu(x):
    y=[]
    for i in x:
        if i>=2:
            for j in range(2,i):
                if i%j==0:
                    continue
                else:
                    y.append(x)
    return y
lst=eval(input())
print(sushu(lst))
