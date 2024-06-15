lst1=eval(input())
lst2=[]
for i in lst1:
    if lst1.count(i)==1:
        lst2.append(i)
lst2.sort()
if lst2==[]:
    print("False")
else:
    print(",".join(map(str,lst2)))

