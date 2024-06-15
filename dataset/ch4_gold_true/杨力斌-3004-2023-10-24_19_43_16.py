def sushu(a):
    x = []
    b = []
    for i in a :
        if i == 2:
            x.append(2)
        elif i >= 2 and i != 9 and i != 27 :
            for j in range(2,i,1):
                if i % j == 0:
                    break
                else:
                    x.append(i)
        elif i == 9 or i == 27:
            pass
    for m in x:
        if m not in b:
            b.append(m)
    print(b)
a = eval(input())
sushu(a)
