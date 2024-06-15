lst=eval(input())
lst1=[]
for x in lst:
    if lst.count(x)==1:
        lst1.append(int(x))
        if len(lst1)!=0:
            lst1.sort()
            print(','.join(map(str,lst1)),end=',')    
        else:
            print(False)
