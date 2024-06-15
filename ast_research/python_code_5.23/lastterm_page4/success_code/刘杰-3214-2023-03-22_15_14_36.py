list==input()
x=list.count(0)
for i in range(x):
    list.remove(0)
for i in range(x):
    list.append(0)
print(list)
