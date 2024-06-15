s = input()
s1 = ''
for x in s:
    if x.isalpha():
        if x.isupper():
            a = 26-(ord(x)-64)+1
            x1 = chr(a+64)
        else:
            a = 26-(ord(x)-96)+1
            x1 = chr(a+96)
        s1 += x1
    else:
        s1 += x
print(s)
print(s1)
