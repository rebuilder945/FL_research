lt=eval(input())
ls=list()
for i in lt:
    if i not in ls:
        lt.remove(i)
        if i not in lt:
            ls.append(i)
for x in ls:
    print(x,end=",")

