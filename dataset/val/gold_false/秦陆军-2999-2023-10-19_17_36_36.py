#【问题描述】

#输入一个由字符串构成的列表和两个整数n和m（n和m在输入列表的下标范围以内），交换其中两个元素的值，打印输出交换后的列表。
#【输入形式】

#第一行输入由空格分隔的多个字符串

#第二行输入两个整数n和m，表示元素的位置，两个数字之间用空格区分。
#【输出形式】

#直接使用print函数输出列表
lst = input().split()
n, m = map(int, input().split())
if 0 <= n < len(lst) and 0 <= m < len(lst):
    lst[n], lst[m] = lst[m], lst[n]
print(lst)
