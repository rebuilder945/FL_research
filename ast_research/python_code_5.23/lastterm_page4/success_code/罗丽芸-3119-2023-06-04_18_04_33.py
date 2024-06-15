ls=eval(input())
ls1=[]
ls.reverse()
for x in ls:
    if x not in ls1:
        ls1.append(x)
    print(ls1)


