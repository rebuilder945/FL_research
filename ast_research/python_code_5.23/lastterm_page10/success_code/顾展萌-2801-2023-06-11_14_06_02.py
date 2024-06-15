
def password_strength(password):
    # 根据规则判断密码强度并计算星级
    stars = 0
    if any(c.isdigit() for c in password):
        stars += 1
    if any(c.islower() for c in password):
        stars += 1
    if any(c.isupper() for c in password):
        stars += 1
    if len(password) >= 8:
        stars += 1
    if any(c in '~!@#$%^&*()_=-/,.?<>;:[]{}|\\' for c in password):
        stars += 1
    return stars

password = input().strip()
print(password_strength(password))

