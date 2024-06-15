lst1=eval(input())
lst1.reverse()
lst2=[' ']
for i in lst1:
    if i not in lst2:
        lst2.insert(0,1)
lst2.pop()
print(lst2)
