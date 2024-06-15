password = input()
stars = 0

# 检查密码是否含有数字字符
if any(char.isdigit() for char in password):
    stars += 1

# 检查密码是否含有小写字母
if any(char.islower() for char in password):
    stars += 1

# 检查密码是否含有大写字母
if any(char.isupper() for char in password):
    stars += 1

# 检查密码长度是否不低于8
if len(password) >= 8:
    stars += 1

# 检查密码是否含有特殊字符
special_chars = "~!@#$%^&*()_=-/,.?<>;:[]{}|\\"
if any(char in special_chars for char in password):
    stars += 1

# 输出密码的星级
print(stars)

