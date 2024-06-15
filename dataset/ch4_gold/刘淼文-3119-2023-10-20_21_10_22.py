lst = eval(input())
lst2 = []
for i in lst[-1::-1]:
    if i in lst2:
        continue
    else:
        lst2.insert(0,i)
print(lst2)

