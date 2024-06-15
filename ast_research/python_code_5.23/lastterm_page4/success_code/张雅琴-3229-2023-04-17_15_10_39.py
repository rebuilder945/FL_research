lst=eval(input())
lst1=[]
for i in lst:
    a=lst.count(i)
    if a >=2:
        lst1.append(i)
        lst1.sort()
        print(lst1)
    else:
        print("False")

