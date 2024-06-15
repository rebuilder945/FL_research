def check(password):
    strength = 0
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if len(password) >= 8:
        strength += 1
    if any(char in "~!@#$%^&*()_=-/,.?<>;:[]{}|\\" for char in password):
        strength += 1
    return strength

password = input()
print(check(password))


