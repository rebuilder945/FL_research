def zhuanhuan(i):
    a = ord(i)
    if 97<=a<=122:
        b = chr(122-a+97)
        return b
    elif 65<=a<=90:
        c = chr(90-a+65)
        return c
    else:
        return i
d = input()
m = ''
for x in d:
    p=zhuanhuan(x)
    m+=p
print(d)
print(m)

