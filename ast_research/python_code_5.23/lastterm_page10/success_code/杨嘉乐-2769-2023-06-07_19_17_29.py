x=input()
l=""
for i in x:
    if ord("a")<=ord(i)<=ord("z"):
        l+=chr(25-(ord(i)-ord("a"))+ord("a"))
    elif ord("A")<=ord(i)<=ord("Z"):
        l+=chr(25-(ord(i)-ord("A"))+ord("A"))    
    else:
        l+=i
print(x)
print(l)
