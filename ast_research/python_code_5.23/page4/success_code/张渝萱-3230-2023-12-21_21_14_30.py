list1 = eval(input())
eva = 0
while len(list1) != 0:
    a = list1[0]
    count = 0   # 记录当前遍历到哪个数字了（0123…
    coun1 = 0   # 记录当前最大的数字的编号
    for x in list1:
        if x > a:
            a = x
            coun1 = count
        count += 1
    eva = 10 * eva + a
print(eva)


