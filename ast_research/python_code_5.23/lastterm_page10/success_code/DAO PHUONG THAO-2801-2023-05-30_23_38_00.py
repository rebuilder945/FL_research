def password_strength(password):
    # 初始化密码强度星级为0
    strength = 0

    # 判断密码是否包含数字字符
    if any(char.isdigit() for char in password):
        strength += 1

    # 判断密码是否包含小写字母
    if any(char.islower() for char in password):
        strength += 1

    # 判断密码是否包含大写字母
    if any(char.isupper() for char in password):
        strength += 1

    # 判断密码长度是否不低于8
    if len(password) >= 8:
        strength += 1

    # 判断密码是否包含特殊字符
    special_chars = "~!@#$%^&*()_=-/,.?<>;:[]{}|\\"
    if any(char in special_chars for char in password):
        strength += 1

    return strength

# 读取输入的密码
password = input()

# 计算密码强度并输出结果
result = password_strength(password)
print(result)



