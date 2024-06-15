x=input()
l=""
for i in x:
    if i.isalpha():
        l+=chr(26-(ord(i)-ord("a"))+ord("a"))
    else:
        l+=i
print(l)
print(x)
