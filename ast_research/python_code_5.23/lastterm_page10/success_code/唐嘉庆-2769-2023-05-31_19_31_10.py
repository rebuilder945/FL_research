def abc(x):
    a=ord(x)-ord('a')
    s=chr(ord('z')-a)
    return s
def ABC(x):
    a=ord(x)-ord('A')
    s=chr(ord('Z')-a)
    return s

x=input()
d = ''
for i in x:
    if 'a' <= i <= 'z':
        d += abc(i)
    elif 'A' <= i <= 'Z':
        d += ABC(i)
    else:
        d += i
print(x)
print(d)

