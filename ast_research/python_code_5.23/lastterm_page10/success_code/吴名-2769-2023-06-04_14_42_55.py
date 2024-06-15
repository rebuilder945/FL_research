def decrypt_password(password):
    decrypted_password = ""
    for char in password:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr(122 - ord(char) + 97)
            else:
                decrypted_char = chr(90 - ord(char) + 65)
        else:
            decrypted_char = char
        decrypted_password += decrypted_char
    return decrypted_password

# 从标准输入获取密码
password = input()

# 解密密码并输出结果
decrypted_password = decrypt_password(password)
print(password)
print(decrypted_password)


