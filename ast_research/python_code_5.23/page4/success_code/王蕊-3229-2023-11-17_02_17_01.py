lst=eval(input())
lst1=[]
for x in lst:
    if lst.count(x)==1:
        lst1.append(x)
lst1.sort()
if lst1:
    print(",".join(str(i) for i in lst1))
else:
    print("False")
