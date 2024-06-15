text = input()  # 输入密码
cipher_text = ""  # 初始化密文
for char in text:
    if char.isalpha():  # 如果是字母
        if char.islower():  # 如果是小写字母
            cipher_text += chr(ord('a') + 25 - (ord(char) - ord('a')))  
            # 将小写字母转为对应的密文字符，具体方法见下方解释
        elif char.isupper():  # 如果是大写字母
            cipher_text += chr(ord('A') + 25 - (ord(char) - ord('A')))
            # 将大写字母转为对应的密文字符，具体方法见下方解释
    else:
        cipher_text += char  # 非字母字符不变


original_text = ""  # 初始化原文
for char in cipher_text:
    if char.isalpha():  # 如果是字母
        if char.islower():  # 如果是小写字母
            original_text += chr(ord('a') + 25 - (ord(char) - ord('a')))  
            # 将密文字符转为对应的原文字符，具体方法同上
        elif char.isupper():  # 如果是大写字母
            original_text += chr(ord('A') + 25 - (ord(char) - ord('A')))
            # 将密文字符转为对应的原文字符，具体方法同上
    else:
        original_text += char  # 非字母字符不变

print(original_text)  # 输出原文
print(cipher_text)  # 输出密文

