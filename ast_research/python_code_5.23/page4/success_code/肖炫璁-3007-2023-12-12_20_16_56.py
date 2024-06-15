# 从输入中获取列表
lst_input = input().strip()
lst = eval(lst_input)

# 从输入中获取n和m
n, m = map(int, input().split(','))

# 判断n和m是否在列表下标范围内
if n <= m and 0 <= n < len(lst) and 0 <= m < len(lst):
    # 删除n~m之间的元素（不包括m位置的元素）
    del lst[n:m]

    # 打印输出列表
    print(lst)
else:
    # 输出错误信息
    print("error")

