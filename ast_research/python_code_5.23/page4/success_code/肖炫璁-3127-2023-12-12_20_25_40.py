# 从键盘读入整数n
n = int(input())

# 使用快速列表生成语法生成列表 [1, 2, ..., n-1, n]
original_list = list(range(1, n + 1))

# 使用for循环将列表循环左移一个位置
shifted_list = [original_list[(i + 1) % n] for i in range(n)]

# 输出循环左移后的列表
print(shifted_list)

