list = eval(input())
i = list.count(0)
if i == 0:
    print(list)
else:
    for x in range(i):
        list.remove(0)
        x -= 1
        list.append(0)
    print(list)

