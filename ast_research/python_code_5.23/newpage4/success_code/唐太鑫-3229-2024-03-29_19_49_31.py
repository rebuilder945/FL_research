lst=list(eval(input()))
lst1=[]
for i in lst:
    if lst.count(i)==1:
        lst1.append(i)
        lst1.sort()
        print(",".join(lst1))
    else:
        print(False)

