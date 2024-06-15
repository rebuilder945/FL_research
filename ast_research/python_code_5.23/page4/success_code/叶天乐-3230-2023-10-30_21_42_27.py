ls1 = eval(input())
ls1.sort(reverse=True)
ls2 = []
for i in ls1:
    if i not in ls2:
        ls2.append(i)
        if ls2[0] == 0:
            print(0)
        else:   
            str1 = ''.join(str1(i) for i in ls1)
            print(str1.join(ls1))
