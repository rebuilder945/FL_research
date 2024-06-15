password = input()
strength = 0

# 含有数字字符
if any(char.isdigit() for char in password):
    strength += 1

# 含有小写字母
if any(char.islower() for char in password):
    strength += 1

# 含有大写字母
if any(char.isupper() for char in password):
    strength += 1

# 长度不低于8
if len(password) >= 8:
    strength += 1

# 至少含有~!@#$%^&*()_=-/,.?<>;:[]{}|\中的一个字符
special_chars = "~!@#$%^&*()_=-/,.?<>;:[]{}|\\"
if any(char in special_chars for char in password):
    strength += 1

print(strength)

