lst = eval(input())
lst2 = []
for i in lst:
    if i not in lst2:
        lst2.append(i)
    else:
        pass
print(lst2)
   
