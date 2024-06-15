lst=eval(input())
lst1=[]
for i in lst:
    if lst.count(i)==1:
        lst1.append(i)
lst1.sort()
if lst1:
    print(",".join(str(a)for a in lst1))
else:
    print("False")
    

