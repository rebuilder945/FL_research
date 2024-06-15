list=eval(input())
a=list.count(0)
if 0 not in list:
    print(False)
else:
    for x in range(a):
        list.remove(0)
for i in range(a):
    list.append(0)
print(list)
