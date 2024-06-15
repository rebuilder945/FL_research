lst1=eval(input())
lst2=lst1.copy()
for x in lst2:
    while True:
        if lst1.count(x)==1:
            break
        else:
            if x in lst1:
                lst1.remove(x)
print(lst1)
