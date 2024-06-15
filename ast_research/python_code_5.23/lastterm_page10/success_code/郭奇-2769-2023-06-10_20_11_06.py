password = input()  # 输入密码

# 解密密码
decrypted_password = ''
for c in password:
    if c.isalpha():
        if c.isupper():
            decrypted_password += chr(26 - (ord(c) - ord('A')) + ord('A') - 1)
        else:
            decrypted_password += chr(26 - (ord(c) - ord('a')) + ord('a') - 1)
    else:
        decrypted_password += c

print(password)  # 输出密码
print(decrypted_password)  # 输出原文
