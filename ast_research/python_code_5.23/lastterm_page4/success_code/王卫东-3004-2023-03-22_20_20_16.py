def sushu(a):
    b =[]
    for x in a:
        if x >= 2:
            for y in range(2,x):
                if x % y ==0:
                    break
            else:
                    b.append(x)
    print(b)
s = eval(input())
sushu(s)    



