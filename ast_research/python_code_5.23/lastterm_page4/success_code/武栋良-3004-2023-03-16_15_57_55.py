ls1 = eval(input())
ls2 = []
for x in lst:
    if x ==2:
        ls2.append(2)
    else:
        for i in range(2,x):
            if x%i:
                ls2.append(x)
            print(ls2)
              
