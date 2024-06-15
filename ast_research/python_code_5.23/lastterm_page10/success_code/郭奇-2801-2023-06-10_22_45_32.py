password = input()  # 输入密码

# 初始化密码强度为0
strength = 0

# 检查是否含有数字字符
if any(char.isdigit() for char in password):
    strength += 1

# 检查是否含有小写字母
if any(char.islower() for char in password):
    strength += 1

# 检查是否含有大写字母
if any(char.isupper() for char in password):
    strength += 1

# 检查密码长度是否不低于8
if len(password) >= 8:
    strength += 1

# 检查是否含有特殊字符
if any(char in '~!@#$%^&*()_=-/,.?<>;:[]{}|\\' for char in password):
    strength += 1

print(strength)  # 输出密码强度星级
