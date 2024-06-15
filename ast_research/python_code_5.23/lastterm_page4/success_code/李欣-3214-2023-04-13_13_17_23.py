lst=eval(input())
lst1=lst.copy()
for i in lst:
    while i==0:
        lst1.remove(0)
        lst1.append(0)
print(lst1)
