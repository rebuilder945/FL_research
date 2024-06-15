list=eval(input())
a=list.count(0)
for x in range(a):
    list.remove(0)
for i in range(a):
    list.append(0)
print(list)
