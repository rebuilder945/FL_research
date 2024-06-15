password = input()

# 初始化密码强度分数和标志变量
score = 0
has_digit = False
has_lower = False
has_upper = False
has_special = False

# 检查密码是否包含数字、小写字母、大写字母和特殊字符
for c in password:
    if c.isdigit():
        has_digit = True
    elif c.islower():
        has_lower = True
    elif c.isupper():
        has_upper = True
    elif c in "~!@#$%^&*()_=-/,.?<>;:[]{}|\\ ":
        has_special = True

# 计算密码的强度分数
if has_digit:
    score += 1
if has_lower:
    score += 1
if has_upper:
    score += 1
if len(password) >= 8:
    score += 1
if has_special:
    score += 1

# 输出密码的强度星级
print(score)
