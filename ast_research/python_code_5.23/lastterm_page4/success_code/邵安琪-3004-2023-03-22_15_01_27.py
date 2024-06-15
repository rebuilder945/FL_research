def sss(y):
    a = []
    for x in y:
        if x>1:
            for i in range(2,x,1):
                if x%i==0:
                    break
            else:
                a.append(x)
    print(a)
b = eval(input())
sss(b)    

