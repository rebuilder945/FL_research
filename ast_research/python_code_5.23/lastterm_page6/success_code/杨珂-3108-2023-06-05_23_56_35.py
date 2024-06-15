a=eval(input())
for i in a:
    for x in range("abcdefghijklmnopqrstuvwxyz"):
        if i.count(x)!=0:
            print(x,",",i.count(x))
        else:
            continue
