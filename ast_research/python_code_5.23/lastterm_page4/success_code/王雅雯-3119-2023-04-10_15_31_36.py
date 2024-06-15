lst=eval(input())
lst1=lst.copy()
for x in lst1:
    ge=lst.count(x)
    if ge>=2:
        for i in range(ge-1):
            lst.remove(x)
print(lst)
