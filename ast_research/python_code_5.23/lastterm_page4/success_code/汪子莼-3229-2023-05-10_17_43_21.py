lst1=eval(input())
lst2=[]
for a in lst1:
    if lst1.count("a")==1:
        lst2.append(a)
lst2.sort()
if lst2:
    print(",".join(str(x) for x in lst2))
else:
    print("False")
