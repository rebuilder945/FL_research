#给定一个字符串，取出第一个没有重复的字符，如果输入为空则输出"None"。
s = input()
flag = False
for i in s:
    if list(s).count(i)==1:
        print(i)
        flag = True
        break
if flag == False:
    print(None)

