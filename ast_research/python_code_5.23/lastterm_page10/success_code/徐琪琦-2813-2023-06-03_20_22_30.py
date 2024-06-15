# 编写一个程序，当在一个字符串中出现指定子串时就删除它。       
s = list(input())
a = list(input())
for i in range(len(s)-len(a)):
    if s[i:i+len(a):]== a:
        del s[i:i+len(a):]
        i += 1
    else: 
        i += 1
print("".join(s))
