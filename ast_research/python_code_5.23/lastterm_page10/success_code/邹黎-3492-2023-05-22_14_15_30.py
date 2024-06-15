a=input()
lst=[]
if a==" ":
    print("None")
else:
    for x in range(0,len(a)):
        lst.append([a.count(a[x]),x])
    for x in range(0,len(lst)):
        if lst[x][0]==1:
            print(a[x])
            break
        elif "1" not in lst[x][0]:
            print("None")
