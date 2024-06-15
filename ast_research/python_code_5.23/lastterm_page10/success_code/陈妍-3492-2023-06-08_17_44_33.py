a=input() or "None"
if a=="None":
    print("None")
else:
    for x in a:
        if a.count(x)==1:
            print(x)
            break



