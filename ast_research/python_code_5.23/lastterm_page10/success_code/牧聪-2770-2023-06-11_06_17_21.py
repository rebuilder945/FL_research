a=input()
b=input()
if len(a)==len(b):
    for x in a:
        if x in b:
            if a.index(x)==len(a)-1:
                print(True)
            else:
                continue
        else:
            print(False)
            break
else:
    print(False)

