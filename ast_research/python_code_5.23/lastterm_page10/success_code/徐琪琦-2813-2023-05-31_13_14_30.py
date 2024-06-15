# 编写一个程序，当在一个字符串中出现指定子串时就删除它。       
s = input().split("")
a = input()
ls = []
if not " " in list(a):
    for i in s:
        if i != a:
            ls.append(i)
    print("".join(ls))
        
        
