def f(x):
    count = 0
    for y in range(2, x):
        if x % y == 0:
            count += 1
    if x == 0 or x == 1:
        return 1  # 不是素数就返回1
    elif count == 0:
        return 0
    elif count != 0:
        return 1


list1 = eval(input())
list2 = []
for x in list1:
    k = f(x)
    if k == 0:
        list2.append(x)
print(list2)

