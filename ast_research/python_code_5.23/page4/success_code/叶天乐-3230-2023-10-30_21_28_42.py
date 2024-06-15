ls1 = eval(input())
ls1.sort(reverse=True)
ls2 = []
for i in ls1:
    if i not in ls2:
        ls2.append(i)
        ls2.remove(0)
        if ls2 == []:
            print(0)
        else:    
            str = ''.join(str(i) for i in ls1)
            print(str)
