a = input()
GDP = {}
while a != 'ok':()
    a = a.split( )
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
