lst=eval(input())
lst.reverse()
lst2=[]
for x in lst:
    if x not in lst2:
        lst2.insert(0,x)
print(lst2)
