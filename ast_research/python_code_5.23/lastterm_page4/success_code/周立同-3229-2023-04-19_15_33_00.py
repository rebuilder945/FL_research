lst=eval(input())
lst1=[]
for i in lst:
    if lst.count(i)==1:
        lst1.append(str(i))
if lst1==[]:
    print("False")
else:
    lst1.sort()
    print(",".join(lst1))
