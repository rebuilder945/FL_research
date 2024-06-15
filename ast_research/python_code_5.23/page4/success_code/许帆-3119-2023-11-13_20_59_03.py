lst1 = eval(input())
lst=[]
for a in lst1:
    if not a in lst:
        lst.append(a)
print(lst)


