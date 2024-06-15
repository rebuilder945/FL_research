lst = eval(input())
for i in lst:
    lst.remove(0)
    lst.append(0)
print(lst)
