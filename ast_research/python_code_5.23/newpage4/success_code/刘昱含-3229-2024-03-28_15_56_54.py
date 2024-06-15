lst=eval(input())
lst1=[]
for i in lst:
    if lst.count(i)==1:
        lst1.append(i)
lst1.sort()
if len(lst1)==0:
    print("False")
else:
    lst2=",".join(map(str,lst1))
    print(lst2)
