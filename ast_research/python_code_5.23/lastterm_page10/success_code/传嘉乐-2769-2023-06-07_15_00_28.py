a=input()
b=''
print(a)
for i in a:
    if 'a'<=i<='z':
        i=chr(2*ord('a')-ord(i)+25)
        b+=i
    elif 'A'<=i<='Z':
        i=chr(2*ord('A')-ord(i)+25)
        b+=i
    else:
        b+=i
print(b)
