lst = eval(input())
for i in range(lst.count(0)):
    a = 0
    lst.remove(0)
    lst.append(a)
print(lst)
