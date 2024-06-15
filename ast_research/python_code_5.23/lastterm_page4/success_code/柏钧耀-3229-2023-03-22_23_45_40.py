lst=eval(input())
lst2=[]
for i in lst :
    a=lst.count(i)
    if a == 1:
        lst2.append(i)
if not lst2:
    print("False")
if lst2: 
    ls3=sorted(lst2)
    print(','.join(str(i)for i in ls3))
