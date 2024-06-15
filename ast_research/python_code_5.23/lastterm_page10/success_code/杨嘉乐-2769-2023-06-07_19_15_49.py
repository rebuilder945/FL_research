x=input()
l=""
for i in x:
    if i.isalpha():
        l+=chr(25-(ord(i)-ord("a"))+ord("a"))
    else:
        l+=i
print(x)
print(l)
