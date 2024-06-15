ls = eval(input())
max_val = max(ls)
min_val = min(ls)

# 找到所有的最大值和最小值的索引
max_indices = [i for i, x in enumerate(ls) if x == max_val]
min_indices = [i for i, x in enumerate(ls) if x == min_val]

# 从后往前遍历所有索引，依次删除元素
for i in sorted(max_indices + min_indices, reverse=True):
    del ls[i]

print(ls)
