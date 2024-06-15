def password_strength(password):
    stars = 0

    if any(char.isdigit() for char in password):
        stars += 1
    if any(char.islower() for char in password):
        stars += 1
    if any(char.isupper() for char in password):
        stars += 1
    if len(password) >= 8:
        stars += 1
    if any(char in "~!@#$%^&*()_=-/,.?<>;:[]{}|\\" for char in password):
        stars += 1

    return stars

# 从标准输入获取密码
password = input()

# 获取密码强度星级并输出结果
result = password_strength(password)
print(result)

