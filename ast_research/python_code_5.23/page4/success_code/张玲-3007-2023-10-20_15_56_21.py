# 读取输入的列表
lst = eval(input())

# 读取n和m并将其转换为整数
n, m = map(int, input().split(','))

# 判断n和m是否在列表下标范围内
if 1 <= n <= len(lst) and 1 <= m <= len(lst) and n <= m:
    del lst[n - 1:m]
    print(lst)
else:
    print("error")

