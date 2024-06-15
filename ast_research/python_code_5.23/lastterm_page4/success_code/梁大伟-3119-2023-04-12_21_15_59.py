lst=eval(input())
lst1=[]
for s in range(len(lst)):
    lst1.append(lst[s])
for i in lst1:
    if lst.count(i)>=2:
        lst.remove(i)
print(lst)
