lst=eval(input())
lst2=[]
for i in lst:
    if not i in lst2:
        lst2.append(i)
print(lst2)
