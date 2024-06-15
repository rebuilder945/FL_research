ls = input()
if len(list(ls))>=1:
    lb =[]
    lc = []
    for a in ls:
        b = ls.count(a)
        if b == 1:
            lb.append(a)
    print(lb[0])
    # for x in lb:
    #     c = ls.index(x)
    #     lc.append(c)
    # print(lb[lc.index(min(lc))])
else:
    print("None")
