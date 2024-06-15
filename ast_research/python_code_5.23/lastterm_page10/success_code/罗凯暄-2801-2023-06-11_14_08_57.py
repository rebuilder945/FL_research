import re

password = input("请输入密码：")

# 检查是否含有数字字符
if re.search(r'\d', password):
    score = 1
else:
    score = 0

# 检查是否含有小写字母
if re.search(r'[a-z]', password):
    score += 1

# 检查是否含有大写字母
if re.search(r'[A-Z]', password):
    score += 1

# 检查密码长度是否不低于8
if len(password) >= 8:
    score += 1

# 检查是否含有特殊字符
if re.search(r'[~!@#$%^&*()_=-/,.?<>;:[]{}|\\]', password):
    score += 1

print("密码强度星级为：", score)

