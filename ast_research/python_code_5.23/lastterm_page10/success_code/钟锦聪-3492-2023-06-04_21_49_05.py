ls = input()
if len(list(ls))>=1:
    lb =[]
    for a in ls:
        b = ls.count(a)
        if b == 1:
            lb.append(a)
    print(lb[0])
else:
    print("None")
