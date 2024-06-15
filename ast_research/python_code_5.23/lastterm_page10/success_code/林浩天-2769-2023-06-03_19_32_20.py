s=input()
s1=''
for i in s:
    if i.isalpha():
        if i.isupper():
            s1+=chr(ord('A')+ord('Z')-ord(i))
        else:
            s1+=chr(ord('a')+ord('z')-ord(i))
    else:
        s1+=i
print(s)
print(s1)

