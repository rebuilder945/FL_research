lst = input().split()  # 读入字符串列表，使用 split() 函数将字符串拆分成单词
n, m = map(int, input().split())  # 读入两个整数，使用 map() 函数将字符串转换成整数

lst[n], lst[m] = lst[m], lst[n]  # 交换两个位置的元素

print(lst)  # 直接输出列表
