lst=eval(input())
lst1=[]
for i in lst:
    if lst.count(i)==1:
        lst1.append(i)
        lst1.sort()
        lst2=list(map(str,lst1))
        print(",".join(lst2))
    else:
        print(False)

