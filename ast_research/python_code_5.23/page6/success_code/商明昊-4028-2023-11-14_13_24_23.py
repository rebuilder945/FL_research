n = eval(input())
ls2 = []
ls3 = []
ls4 = []
if n<=1 or type(n)!=int:
    print('illegal input')
else:
    ls = [x for x in range(2,n+1)]
    for i in ls:
        for p in range(2,i):
            if i%p==0:
                ls2.append(i)
    for x in ls:
        if x not in ls2:
            ls3.append(x)
    for y in ls3:
        if str(y)[0] == str(y)[-1]:
            ls4.append(y)
    ls4 = " ".join(map(str,ls4))
    print(ls4)

