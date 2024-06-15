lst=eval(input())
lst1=lst.copy()
d=0
for i in lst1:
    if lst1.count(i)==1:
        d=d+1
        lst.append(i)
        lst.sort()
        if d==0:
            print(False)
    print(lst)

        

        


