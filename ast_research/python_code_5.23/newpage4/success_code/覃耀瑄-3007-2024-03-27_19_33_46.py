list1 = eval(input())
n, m = map(int, input().split(','))

# 获取列表的最大值和最小值
min_val = min(list1)
max_val = max(list1)

# 检查 n 和 m 是否在列表的范围内
if min_val <= n <= max_val and min_val <= m <= max_val and n <= m:
    # 删除 n 到 m 之间的元素（不包括 m）
    new_list = [x for x in list1 if x < n or x >= m]
    print(new_list)
else:
    print("error")

