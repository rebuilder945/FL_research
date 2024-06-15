lst1=eval(input())
lst2=[]
for i in lst1:
    if i not in lst2:
        lst2.append(i)
lst2.sort()
if lst2==[]:
    print(False)
else:
    print(lst2)

