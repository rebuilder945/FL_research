lst=eval(input())
lst1=lst.copy()
for x in lst1:
    if x==0:
        del(x)
        lst.append(0)
print(lst1)
