lst1=eval(input())
lst2=lst1.copy()

for i in lst1:
    if lst2.count(i)>1:
        lst2.remove(i)

print(lst2)
    

