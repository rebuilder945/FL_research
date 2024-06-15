lst1=[]
lst2=input()
lst2.reverse()
for i in lst2:
    if i not in lst1:
        lst1.append(i)
print(lst1)
