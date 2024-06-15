# 若继续删除子串
s = input()
s1 = input()
while s1 in s:
    s = s.replace(s1,"")
print(s)
