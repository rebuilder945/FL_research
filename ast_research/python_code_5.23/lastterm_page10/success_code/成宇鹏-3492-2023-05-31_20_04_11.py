# 给定一个字符串，取出第一个没有重复的字符，如果输入为空则输出"None"。
from itertools import count


s = input()
a = len(s)
for x in range(a):
    if s.count(s[x]) != 1:
        pass
    elif s.count(s[x]) == 1:
        print(s[x])
        break
    else:
        print("None")
