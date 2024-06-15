lst=eval(input())
lst.reverse()
lst2=[]
for i in lst:
    if i not in lst2:
        lst2.append(i)
lst2.reverse()
print(lst2)
