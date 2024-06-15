a=eval(input())
for i in a:
    for x in "abcdefghijklmnopqrstuvwxyz":
        if i.count(x)!=0:
            print(x,",",i.count(x),end="")
        else:
            continue
