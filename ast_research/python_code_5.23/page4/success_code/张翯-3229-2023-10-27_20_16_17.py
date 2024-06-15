lst1=eval(input())
lst2=[]

for i in lst1:
    if lst1.count(i)==1:
        lst2.append(i)
if lst2==[]:
    print("False")
else:
    lst2.sort()
    lst3=[str(x) for x in lst2]
    a=','.join(lst3)
    print(a)
