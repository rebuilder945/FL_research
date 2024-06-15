lst=eval(input())
lst2=lst.copy
for i in lst:
    a=lst.count(i)
    a=int(a)
    if a>=2:
        lst2.remove(i)
        if lst2==False:
            print("False")
        else:
            lst2.sort()
            print(lst2)
