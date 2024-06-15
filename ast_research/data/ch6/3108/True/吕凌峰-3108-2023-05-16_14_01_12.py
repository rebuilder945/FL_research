#  题库：统计字符串列表中每个字母出现的次数 - Python编程基础及应用》习题6-8
# 【问题描述】
# 统计字符串列表中每个字母出现的次数。
# 编写程序，使用eval()函数读入一个仅包含字符串对象的列表，然后统计该列表中每个字母出现的次数。
# 列表中的字符串对象仅包含小写英文字母。

lst = eval(input())
x = ''.join(lst)
for i in 'abcdefghijklmnopqrstuvwxyz':
    if i in x:
        l = i + ',' + str(x.count(i))
        print(l)
