lst = eval(input())
lst.sort(reverse = True)
lst1 = []
for i in lst:
    if i not in lst1:
        lst1.append(i)
lst1.sort(reverse = True)
print(lst1)

