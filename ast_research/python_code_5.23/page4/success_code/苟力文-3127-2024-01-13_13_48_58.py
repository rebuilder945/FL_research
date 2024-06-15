# 从键盘读入一个整数n
n = int(input())

# 使用快速列表生成语法生成列表 [1, 2, ... ,n-1, n]
lst = list(range(1, n)) + [n]

# 使用for循环将列表循环左移一个位置
for i in range(n - 1):
    lst[i], lst[i + 1] = lst[i + 1], lst[i]

# 输出循环左移后的列表
print(lst)

