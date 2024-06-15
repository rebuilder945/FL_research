lst=eval(input())
lst1=[]
for i in lst:
    if lst.count(i)!=1:
        print("False")
    else:
        if lst.count(i)==1:
            lst1.append(i)
            print(lst1)

