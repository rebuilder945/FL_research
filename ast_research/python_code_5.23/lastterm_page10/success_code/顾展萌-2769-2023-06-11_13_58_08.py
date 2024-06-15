
def decode(s):
    res = ''
    for c in s:
        if c.isalpha():
            if c.isupper():
                res += chr(ord('A') + 25 - (ord(c) - ord('A')))
            else:
                res += chr(ord('a') + 25 - (ord(c) - ord('a')))
        else:
            res += c

    return res

s = input().strip()
print(s)
print(decode(s))

