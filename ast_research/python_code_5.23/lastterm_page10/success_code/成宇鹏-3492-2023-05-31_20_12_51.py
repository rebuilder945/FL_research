# 给定一个字符串，取出第一个没有重复的字符，如果输入为空则输出"None"。
from itertools import count


s = input()
lst = []
for x in s:
    if s.count(x) != 1:
        lst.append(s.count(x))
    else:
        lst.append(s.count(x))
        print(x)
        break
if 1 not in lst:
    print("None")
