s = input().strip()  # 输入字符串并去除两端空格
sub = input().strip()  # 输入子串并去除两端空格

while sub in s:  # 只要子串还在字符串中就继续循环
    s = s.replace(sub, '')  # 用 '' 替换掉子串
print(s)
