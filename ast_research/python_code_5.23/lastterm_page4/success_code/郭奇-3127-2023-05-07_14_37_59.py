n = int(input())  # 读入整数n

# 使用快速列表生成语法生成列表 [1, 2, ... ,n-1, n]
my_list = list(range(1, n+1))

# 使用for循环将列表循环左移一个位置
first_element = my_list[0]
for i in range(n-1):
    my_list[i] = my_list[i+1]
my_list[n-1] = first_element

# 输出循环左移后的列表
print(my_list)
