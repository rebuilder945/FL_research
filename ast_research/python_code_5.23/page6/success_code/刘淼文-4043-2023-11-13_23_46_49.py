lst = list(str(input()))
for x in "abcdefghijklmnopqrstuvwxyz":
    if x in lst:
        n = lst.count(x)
        tmp = x+','+str(n)
        print(tmp)
