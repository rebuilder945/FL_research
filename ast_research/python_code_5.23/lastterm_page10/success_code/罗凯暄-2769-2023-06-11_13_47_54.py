password = input()  # 读取密码字符串

original = ''  # 初始化原文字符串

for char in password:
    if char.isalpha():  # 如果是字母
        if char.isupper():  # 如果是大写字母
            original += chr(155 - ord(char))  # 转换为原来的字母
        else:  # 如果是小写字母
            original += chr(219 - ord(char))  # 转换为原来的字母
    else:  # 如果不是字母
        original += char  # 保持不变

print(password)  # 输出密码
print(original)  # 输出原文

