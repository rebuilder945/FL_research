lst=eval(input())
lst.sort()
lst1=[]
for i in lst:
    if i not in lst1:
        lst1.append(i)
lst2=[]
for i in lst1:
    num=lst.count(i)
    if num==1:
        lst2.append(i)
if bool(lst2)==True:
    i=[str(x) for x in lst2]
    print(",".join(i))
else:
    print("False")
