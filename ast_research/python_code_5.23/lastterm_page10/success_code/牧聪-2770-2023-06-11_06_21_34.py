a=input()
b=input()
if len(a)==len(b):
    time=-1
    for x in a:
        time+=1
        if x in b:
            if time==len(a)-1:
                print(True)
            else:
                continue
        else:
            print(False)
            break
else:
    print(False)

