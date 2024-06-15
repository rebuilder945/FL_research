# 【问题描述】

# 输入一个由字符串构成的列表和两个整数n和m（n和m在输入列表的下标范围以内），交换其中两个元素的值，打印输出交换后的列表。
# 【输入形式】

# 第一行输入由空格分隔的多个字符串

# 第二行输入两个整数n和m，表示元素的位置，两个数字之间用空格区分。
# 【输出形式】

# 直接使用print函数输出列表
# 【样例输入1】

# hello world python is great

# 2 3
# 【样例输出1】

# ['hello', 'world', 'is', 'python', 'great']

# 【样例输入2】

# hello world python is great

# -2 3
# 【样例输出2】

# ['hello', 'world', 'python', 'is', 'great']

# 【样例说明】

# 多个字符串由空格区分，程序读入后，转变成列表，然后交换指定位置的元素，最后使用print直接输出列表。

ls=input().split()
[n,m]=input().split()
n=int(n)
m=int(m)
ls[n],ls[m]=ls[m],ls[n]
print(ls)

