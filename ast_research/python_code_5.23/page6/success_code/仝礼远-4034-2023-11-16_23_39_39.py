m=input()
n=input()
if m=='red' and n=='blue' or m=='blue' and n=='red':
    print('purple')
if m=='red' and n=='yellow' or m=='yellow' and n=='red':
    print('orange')
if m=='yellow' and n=='blue' or m=='blue' and n=='yellow':
    print('green')
if m==n or n not in ['red','blue','yellow'] or m not in ['red','blue','yellow']:
    print('error')
