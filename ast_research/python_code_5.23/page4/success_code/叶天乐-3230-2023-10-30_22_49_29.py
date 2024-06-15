ls1 = eval(input())
ls1.sort(reverse=True)
ls2 = []
for i in ls1:
    if i not in ls2:
        ls2.append(i)
        if ls2[0] != 0:
            result = ''.join(str(i) for i in ls1)
            print(result)
        else:   
            print(0)
