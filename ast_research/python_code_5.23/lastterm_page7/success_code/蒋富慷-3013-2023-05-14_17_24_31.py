a = input().split( )
GDP = {}
while a != ['ok']:
    b,c = a
    c = int(c)
    GDP[b] = c
    a = input().split( )
d = list(GDP.keys())
d.sort()
e = list(GDP.values())
e.sort()
f = sum(e)
print(d)
print(e)
if 'India' in d:
    print('yes')
else:
    print('no')
print(f)
