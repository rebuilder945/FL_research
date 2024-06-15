string = input()
decrypt_string = ""
for char in string:
    if not char.isalpha():
        decrypt_string += char
    elif char.isupper():
        decrypt_string += chr(ord('A') + ord('Z') - ord(char))
    else:
        decrypt_string += chr(ord('a') + ord('z') - ord(char))
print(string)
print(decrypt_string)
