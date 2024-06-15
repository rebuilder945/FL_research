a = input().split( )
GDP = {}
while a != 'ok':
    b,c = a
    c = int(c)
    GDP[b] = c
    a = input()
d = list(GDP.keys())
e = list(GDP.values())
f = sum(e)
print(d)
print(e)
if 'India' in d:
    print('yes')
else:
    print('no')
print(f)
