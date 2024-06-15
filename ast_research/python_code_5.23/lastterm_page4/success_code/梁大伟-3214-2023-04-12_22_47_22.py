lst1=eval(input())
lst2=[]
for i in lst1:
    if i != 0:
        lst2.append(i)
for s in range(lst1.count(0)):
    lst2.append(0)
print(lst2)
