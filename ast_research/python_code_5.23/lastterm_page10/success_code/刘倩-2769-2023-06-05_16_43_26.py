password = input()  # 输入一串密码

decrypted_password = ""  # 用于存储解密后的密码
for char in password:
    if char.isalpha():  # 判断字符是否为字母
        if char.isupper():  # 判断字符是否为大写字母
            decrypted_password += chr(90 - (ord(char) - 65))  # 将大写字母转换为原文的对应字母
        else:
            decrypted_password += chr(122 - (ord(char) - 97))  # 将小写字母转换为原文的对应字母
    else:
        decrypted_password += char  # 非字母字符不作变换，直接添加到解密后的密码中

print(password)  # 输出密码
print(decrypted_password)  # 输出解密后的原文

