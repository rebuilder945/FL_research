# 编写一个程序，当在一个字符串中出现指定子串时就删除它。       
import copy
s = list(input())       #不可以用.split(""),那么就会ValueError: empty separator
a = input()
ls = []
i = j = 0
flag = True
start = 0
s1 = copy.deepcopy(s)  #不可以一遍遍历一遍删除，要用deepcopy必须有import copy，而且list不可以deepcopy
while i < len(a) and j < len(s):
    if a[i] == s[j]:
        start = j
        if len(a) > len (s) -j-1:
            break
        else:
            for x in range(len(a)-i-1):
                i += 1
                j += 1
                if a[i] != s[j]:
                    flag = False
                    break
            if flag:
                del s1[start:start + len(a):]
    else:
        j += 1
print("".join(s1))
