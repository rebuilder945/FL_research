s = input().strip()    # 去除输入字符串收尾的空白字符
t = input().strip()    # 去除输入子串的收尾空白字符
while t in s:
    s = s.replace(t, '')
    break
print(s)
