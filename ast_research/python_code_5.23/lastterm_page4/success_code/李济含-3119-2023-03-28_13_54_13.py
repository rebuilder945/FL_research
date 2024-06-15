lst1=eval(input())
lst1.reverse()
lst2=[]
for x in lst1:
    if x not in lst2:
        lst2.insert(0,x)
print(lst2)


