lst=eval(input())
lst1=lst.copy()
for x in lst:
    if x==0:
        lst1.remove(0)
        lst1.append(0)
print(lst1)
