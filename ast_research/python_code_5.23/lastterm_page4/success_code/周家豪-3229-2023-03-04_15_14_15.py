lst1=eval(input())
lst2=[]

for i in lst1:
    if lst1.count(i)==1:
        lst2.append(i)

if len(lst2)!=0:
    lst2.sort(reverse=False)
    print(",".join(str(i) for i in lst2))
else:
    print(False)
