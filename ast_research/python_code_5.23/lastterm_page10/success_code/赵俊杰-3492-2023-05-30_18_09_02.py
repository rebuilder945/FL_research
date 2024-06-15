str=input()
if len(str)==0:
    print("None")
else:
    for x in str:
        if str.count(x)==1:
            print(x)
            break
        else:
            pass

