# 输入一个由字符串构成的列表和两个整数n和m（n和m在输入列表的下标范围以内），交换其中两个元素的值，打印输出交换后的列表。

lst = input().split()
n,m = eval(input())
a = lst[n]
b = lst[m]
lst[n]= b
lst[m] =a
print(lst)
