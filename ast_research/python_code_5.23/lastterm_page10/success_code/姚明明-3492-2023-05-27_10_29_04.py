a=input() or "None"
if a=="None":
    print(a)
else:
    for x in a:
        if a.count(x)==1:
            print(a)
            break
