lst = eval(input())
n = lst.count(0)
for  x in range(n):
    lst.remove(0)
for  x in range(n):
    lst.append(0)
print(lst)
