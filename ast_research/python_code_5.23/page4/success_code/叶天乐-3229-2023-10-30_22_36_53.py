ls1 = eval(input())
ls2 = []
for i in ls1:
    if count(i)>1:
        if i not in ls2:
            ls2.append(i)
            print(ls2)
    else:
        print("False")


