lst1=eval(input())
lst2=lst1.copy()
for x in lst1:
    a=lst2.count(x)
    if a>1:
        while a>1:
            lst2.remove(x)
            a-=1
print(lst2)

