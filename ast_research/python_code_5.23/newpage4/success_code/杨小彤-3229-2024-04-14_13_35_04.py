ls = eval(input())
ls1 = []
for x in ls:
    if ls.count(x) == 1:
        ls1.append(x)
        ls1.sort()
        print(",".join (ls1))
else:
    print("False")



