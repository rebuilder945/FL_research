#输入一个由字符串构成的列表和两个整数n和m（n和m在输入列表的下标范围以内），交换其中两个元素的值，打印输出交换后的列表。
lst = input().split()
n,m = input().split()
lst = list(lst)
n = int(n)
m = int(m)
lst[n],lst[m] = lst[m],lst[n]
print(lst)
