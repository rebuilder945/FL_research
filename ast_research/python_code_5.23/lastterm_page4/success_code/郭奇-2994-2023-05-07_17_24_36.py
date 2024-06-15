lst = input().split(',')  # 输入列表元素，用逗号分隔
n, m = map(int, input().split(','))  # 输入n和m

if n < -len(lst) or n >= len(lst):  # 判断n是否在列表下标范围之内
    print("error")
else:
    lst.append(lst[n]*m)  # 将第n个元素重复m次加入列表尾部
    print(lst)


