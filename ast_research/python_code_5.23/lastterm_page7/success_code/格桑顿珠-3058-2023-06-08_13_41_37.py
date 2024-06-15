# 统计字符串出现的次数（字典-2）
# 【问题描述】
# 编写一个程序，从键盘读取未指定个数的字符串，一行一个，以字符串"q"为输入结束标志（"q"不列入统计范围）。
# 使用字典找出其中出现次数最多的字符串，打印该字符串及其出现次数。 
# 注意：本题的测试用例中将保证只有一个字符串出现次数最多，且至少有一条数

s = input()
dic = {}
while s != 'q':
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1
    s = input()
items = []
for x, y in dic.items():
    items.append([x, y])
items.sort(key = lambda x: x[1], reverse = True)
print("%s %i" %(items[0][0], items[0][1]))

