# 编写一个程序读取未指定个数的字符串(以空格隔开)，找出出现次数最多的字符串及其出现次数。
# 如果出现次数最多的有多个字符串，按照字符串升序输出所有出现次数最多的字符串。
# 例如输入abc bcd abc bcd bbb,那么字符串"abc"和"bcd"出现的次数最多，2次，先输出abc 2，再输出bcd 2。
s = input().split()
dic = {}
for i in s:
    dic[i] = dic.get(i,0) + 1
for i in dic:
    if dic[i] == max(dic.values()):
        print(max(dic,key = dic.get),max(dic.values()))



