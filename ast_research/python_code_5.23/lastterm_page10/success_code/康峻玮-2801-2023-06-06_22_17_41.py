password = input()
level = 0
# 检查数字字符
if any(char.isdigit() for char in password):
    level += 1
# 检查小写字母
if any(char.islower() for char in password):
    level += 1
# 检查大写字母
if any(char.isupper() for char in password):
    level += 1
# 检查长度
if len(password) >= 8:
    level += 1
# 检查特殊字符
special_chars = '~!@#$%^&*()_=-/,.?<>;:[]{}|\\'
if any(char in special_chars for char in password):
    level += 1
print(level)
