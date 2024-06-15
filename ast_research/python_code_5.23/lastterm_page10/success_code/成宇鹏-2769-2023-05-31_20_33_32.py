s = input()
n = ''
for x in s:
    if 'a'<= x <= 'z':
        n += chr(ord('z')-ord(x)+ord('a'))
    elif 'A'<= x <='Z':
        n += chr(ord('Z')-ord(x)+ord('A'))
    else:
        n += x
print(s)
print(n)
