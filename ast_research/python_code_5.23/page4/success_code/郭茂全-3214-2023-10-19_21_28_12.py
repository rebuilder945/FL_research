list=eval(input())
if 0 not in list:
    print(False)
else:
    for x in range(list.count(0)):
        list.remove(0)
for i in range(list.count(0)):
    list.append(0)
print(list)
