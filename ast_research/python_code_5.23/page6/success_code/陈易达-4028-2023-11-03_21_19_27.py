n = eval(input())
if type(n) != int or n <= 1:
    print("illegal input")
else:
    ls = []
    for x in range(2,n+1):
        for i in range(2,x):
            if x%i == 0:
                ls.append(x)
    ls2 = []
    for x in ls:
        if x not in ls2:
            ls2.append(x)
    ls3 = []
    for x in ls2:
        if str(x)[0] == str(x)[-1]:
            ls3.append(x)
    print(" ".join(map(str,ls3)))

