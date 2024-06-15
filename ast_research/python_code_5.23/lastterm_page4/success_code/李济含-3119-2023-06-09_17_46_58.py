lst1=eval(input())
lst1.reverse()
lst2=[]
for x in lst1:
    if x not in lst2:
        lst2.append(x)
lst3=lst2.reverse()
print(lst2)
