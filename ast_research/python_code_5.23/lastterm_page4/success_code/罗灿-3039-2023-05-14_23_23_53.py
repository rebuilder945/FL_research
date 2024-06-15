lst=input()
lst1=[]
b=max(lst1)
c=min(lst1)
for x in lst:
    a=lst.count(x)
    lst1.append(a)
for a in lst1:
    if a==b or a==c:
        lst.remove(x)
        print(lst)
