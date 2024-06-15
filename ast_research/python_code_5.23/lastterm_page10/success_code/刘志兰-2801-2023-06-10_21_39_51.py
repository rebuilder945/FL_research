password = input()

digits = any(c.isdigit() for c in password)
lowercase = any(c.islower() for c in password)
uppercase = any(c.isupper() for c in password)
length = len(password) >= 8
special = any(c in '~!@#$%^&*()_=-/,.?<>;:{}[]|\\' for c in password)

score = digits + lowercase + uppercase + length + special

print(score)
