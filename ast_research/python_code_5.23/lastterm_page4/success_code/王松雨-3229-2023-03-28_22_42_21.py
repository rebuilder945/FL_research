lst=eval(input())
for x in lst:
    if lst.count(x)==1:
        lst1=[]
        lst1.append(x)
        lst1.sort()
        if len(lst1)!=0:
            print(','.join(map(str,lst1)),end=',')
        else:
            print(False)
