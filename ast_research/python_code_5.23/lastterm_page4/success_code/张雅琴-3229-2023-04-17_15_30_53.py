lst=eval(input())
for i in lst:
    a=lst.count(i)
    a=int(a)
    if a>=2:
        lst.remove(i)
        if lst==False:
            print("False")
        else:
            lst.sort()
            print(lst)
