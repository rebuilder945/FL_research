# 统计字符串的出现次数（字典-3）
# 【问题描述】
# 编写一个程序读取未指定个数的字符串(以空格隔开)，找出出现次数最多的字符串及其出现次数。
# 如果出现次数最多的有多个字符串，按照字符串升序输出所有出现次数最多的字符串。
# 例如输入abc bcd abc bcd bbb
# 那么字符串"abc"和"bcd"出现的次数最多，2次，先输出abc 2，再输出bcd 2.

lst = list(input().split(' '))
dic = {}
for i in lst:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
items = []
for x, y in dic.items():
    items.append([x, y])
items.sort(key = lambda x: x[1], reverse = True)
items.sort(key = lambda x: x[0])
for i in items:
    if i[1] == items[0][1]:
        print('%s %i' %(i[0], i[1]))
