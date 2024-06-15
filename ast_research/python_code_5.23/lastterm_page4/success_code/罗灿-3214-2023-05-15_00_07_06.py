lst1=list(input())
lst2=[]
for i in lst1:
    if i!=0:
        lst2.append(i)
zero=lst1.count(0)
lst0=0*zero
lst2.append(lst0)
print(lst2)
