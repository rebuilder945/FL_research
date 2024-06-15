ls1 = "".join(eval(input()))
for x in "abcdefghijklmnopqrstuvwxyz":
    if x in ls1:
        num = ls1.count(x)
        tmp = x+","+str(num)
        print(tmp)

