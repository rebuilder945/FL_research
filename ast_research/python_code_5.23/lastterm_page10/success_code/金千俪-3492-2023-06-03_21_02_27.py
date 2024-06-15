a=input()
if a ==" ":
    print("None")
else:
    lst=[]
    for i in a:
        if a.count(i)==1:
            lst.append(i)
    if len(lst)!=0:
        print(lst[0])
    else:
        print("None")
