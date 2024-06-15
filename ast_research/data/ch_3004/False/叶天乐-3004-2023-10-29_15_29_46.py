ls1 = eval(input())
ls2 = []
for i in ls1:
    if i == 2:
        ls2.append(2)
    else:
        for m in range(2,i//2+1):
            if i%m == 0:
                break
            else:
                ls2.append(i)
print(ls2)


