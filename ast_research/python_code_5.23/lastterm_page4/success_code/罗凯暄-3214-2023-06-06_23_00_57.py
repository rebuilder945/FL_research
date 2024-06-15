list = eval(input())
for x in list:
    if x == 0:
        list.remove(x)
        list.append(x)
print(list)
