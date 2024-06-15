a = input()
ls = []
if a == "":
    print("None")
else:
    for i in range(0,len(a)):
        ls.append(a[i])
    for x in ls:
        if ls.count(x)==1:
            print(x)
            break
