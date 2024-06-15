

# # 从键盘读入整数 n
# n = int(input())

# # 使用快速列表生成语法生成列表 [1, 2, ... , n]
# original_list = list(range(1, n + 1))

# # 使用for循环将列表循环左移一个位置
# # 我们将使用切片操作来实现列表的循环左移
# for i in range(n):
#     # 将第一个元素移动到最后的位置
#     original_list.append(original_list.pop(0))

# 输出循环左移后的列表
# print(original_list)

a = int(input())
b = list(range(1,a+1))
for i in range(a):
    b.append(b.pop(0))
print(b)


