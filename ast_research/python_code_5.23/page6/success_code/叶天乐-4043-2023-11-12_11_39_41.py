a = eval(input())
for x in "abcdefghijklmnopqrstuvwxyz":
    if x in a:
        num = a.count(x)
        tmp = x+","+str(num)
        print(tmp)

