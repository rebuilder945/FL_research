list = eval(input())
a = max(list)
b = min(list)
list1 = []
for x in range(0,len(list)):
    if list[x] == a or list[x] == b:
        list1.append(list[x])
    list.sort()
print(list)

