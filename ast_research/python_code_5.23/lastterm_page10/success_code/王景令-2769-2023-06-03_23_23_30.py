a = input()
b = a
c = ''
for i in range(len(a)):
    if ord('a') <= ord(a[i]) <= ord('z'):
        c += chr(ord('a') + ord('z')-ord(a[i]))
    elif ord('A') <= ord(a[i]) <= ord('Z'):
        c += chr(ord('A')+ord("Z")-ord(a[i]))
    else:
        c += a[i]
print(b)
print(c)

