m=input()
n=''
for i in m:
    if  'a'<=i<='z':
        n+=chr(ord('z')-ord(i)+ord('a'))
    elif 'A'<=i<='Z':
        n+=chr(ord('Z')-ord(i)+ord('A'))
    else:
        n+=i
print(m)
print(n)


