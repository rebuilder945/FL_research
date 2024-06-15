def check_password_strength(password):
    strength = 0
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if len(password) >= 8:
        strength += 1
    special_chars = "~!@#$%^&*()_=-/,.?<>;:[]{}|\\"
    if any(char in special_chars for char in password):
        strength += 1
    return strength
password = input()
strength = check_password_strength(password)
print(strength)
