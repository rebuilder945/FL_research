lst=eval(input())
lst.reverse()
lst2=[""]
for i in lst:
    if i not in lst2:
        lst2.insert(0,i)
lst2.pop()
print(lst2)
