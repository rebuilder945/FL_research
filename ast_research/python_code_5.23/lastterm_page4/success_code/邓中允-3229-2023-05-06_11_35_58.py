lst=eval(input())
lst.sort()
lst1=lst.copy()
for i in lst:
    if i in lst1:
        lst1.remove(i)
        print(lst1)
    else:
        print("False")
