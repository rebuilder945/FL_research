lst1=eval(input())
lst2=[]
for x in lst1:
    if not x in lst2:
        lst2.append(x)
print(lst2)
