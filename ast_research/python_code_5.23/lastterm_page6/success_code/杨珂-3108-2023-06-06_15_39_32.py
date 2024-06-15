a=eval(input())
for i in a:
    for x in "abcdefghijklmnopqrstuvwxyz":
        if i.count(x)!=0:
            print(x,end="")
            print(",",end="")
            print(i.count(x))
        else:
            continue
