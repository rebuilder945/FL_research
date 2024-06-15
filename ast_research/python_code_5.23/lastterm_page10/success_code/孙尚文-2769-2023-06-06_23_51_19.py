
lst=input()
a=''
for i in range(len(lst)):
    if 'a'<= lst[i]<= "z":
        a+=chr((ord('z'))-ord(lst[i])+ord('a'))
    elif 'A'<= lst[i]<= "Z":
        a+=chr((ord('Z'))-ord(lst[i])+ord('a'))
    else:
        a+=lst[i]
print(lst)
print(a)

