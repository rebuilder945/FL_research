def decrypt(s):
    result = ""
    for c in s:
        if c.isalpha():
            if c.islower():
                new_c = chr(ord('a') + ord('z') - ord(c))
            else:
                new_c = chr(ord('A') + ord('Z') - ord(c))
        else:
            new_c = c
        result += new_c
    return result

# 测试代码
s = input()
encrypted = s
decrypted = decrypt(s)
print(encrypted)
print(decrypted)
