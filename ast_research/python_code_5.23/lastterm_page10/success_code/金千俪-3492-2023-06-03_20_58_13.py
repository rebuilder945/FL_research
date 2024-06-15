a=input()
if a ==" ":
    print("None")
else:
    lst=[]
    for i in a:
        if a.count(i)==1:
            lst.append(i)
    print(lst[0])
