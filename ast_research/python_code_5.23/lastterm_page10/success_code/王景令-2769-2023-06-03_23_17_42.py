a = input()
c = ''
for i in range(len(a)):
    if ord('a') <= ord(a[i]) <= ord('z'):
        c += chr(ord('z')-ord(a[i])+1)
    elif ord('A') <= ord(a[i]) <= ord('Z'):
        c += chr(ord("Z")-ord(a[i]+1))
    else:
        c += i
print(a)

