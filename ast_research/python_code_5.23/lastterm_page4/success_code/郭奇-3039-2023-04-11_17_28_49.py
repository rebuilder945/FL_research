lst = eval(input())
# 找到最大值和最小值
max_val = max(lst)
min_val = min(lst)

# 删除所有的最大值和最小值
while max_val in lst:
    lst.remove(max_val)
while min_val in lst:
    lst.remove(min_val)

# 输出结果
print(lst)
