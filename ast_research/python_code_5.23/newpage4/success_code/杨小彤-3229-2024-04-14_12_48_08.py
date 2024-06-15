def nums(ls):
    ls1 = []
    for x in ls:
        if ls.count(x) == 1:
            ls1.append(x)
        ls1.sort()
        return ",".join (ls1)
    else:
        return False
ls = eval(input())
a = nums(ls)
print(a)



