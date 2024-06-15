a=input()
lst=list(a)
if len(lst)==0:
    print("None")
else:
    for i in lst:
        if lst.count(i)==1:
            print(i)
            break

