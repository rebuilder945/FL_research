def decrypt_password(password):
    original_text = ""
    for char in password:
        if char.isupper():
            original_text += chr(155 - ord(char))
        elif char.islower():
            original_text += chr(219 - ord(char))
        else:
            original_text += char
    return original_text
password = input()
original_text = decrypt_password(password)
print(password)
print(original_text)

