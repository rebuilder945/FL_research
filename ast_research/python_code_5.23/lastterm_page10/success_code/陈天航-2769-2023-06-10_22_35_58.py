password = input()
result = ''
for char in password:
    if char.isalpha():
        original_pos = 25 - (ord(char.lower()) - ord('a'))
        if char.isupper():
            result += chr(ord('A') + original_pos)
        else:
            result += chr(ord('a') + original_pos)
    else:
        result += char
print(password)
print(result)

