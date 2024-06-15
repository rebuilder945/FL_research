# 输入列表和 n, m
lst = list(map(int, input().split(',')))
n, m = map(int, input().split(','))

# 判断 n 是否在列表范围内，然后执行相应操作
if abs(n) < len(lst):
    element = lst[n]
    lst.extend([element] * m)
else:
    print("error")

# 输出列表
print(lst)

