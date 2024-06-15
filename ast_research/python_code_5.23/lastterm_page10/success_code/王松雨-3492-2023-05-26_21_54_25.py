a=input() or 1
if a==1:
    print("None")
else:
    for i in a:
        lst=[]
        if a.count(i)==1:
            lst.append(i)
            print(lst[0])
           
