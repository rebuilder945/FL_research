cipher_text = input()  # 输入密码
plain_text = ''        # 初始化原文为空字符串

for char in cipher_text:
    if char.isalpha():              # 如果是字母字符
        if char.isupper():          # 大写字母
            plain_text += chr(ord('A') + (ord('Z') - ord(char)))  # 计算成对应的字母
        else:                       # 小写字母
            plain_text += chr(ord('a') + (ord('z') - ord(char)))
    else:                           # 非字母字符
        plain_text += char          # 直接添加到原文中
        
print(cipher_text)   # 输出密码
print(plain_text)    # 输出原文
