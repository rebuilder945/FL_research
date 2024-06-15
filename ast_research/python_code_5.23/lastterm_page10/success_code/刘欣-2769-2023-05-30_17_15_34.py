password = input()
plain_text = ''
for char in password:
    if char.isalpha():
        plain_text += chr(26 - ord(char.lower()) + 97)
    else:
        plain_text += char
print(password)
print(plain_text)
