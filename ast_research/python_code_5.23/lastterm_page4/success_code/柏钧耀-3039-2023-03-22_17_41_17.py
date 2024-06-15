a = eval(input())

if a == []:
    print([])
else:
    max_val = max(a)
    min_val = min(a)

    # 统计最大值和最小值的个数
    max_count = a.count(max_val)
    min_count = a.count(min_val)

    # 删除最大值和最小值
    a = [x for x in a if x != max_val and x != min_val]

    # 删除多余的最大值和最小值
    for i in range(max_count - 1):
        a.remove(max_val)
    for i in range(min_count - 1):
        a.remove(min_val)

    print(a)

