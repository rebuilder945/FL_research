x=input()
l=""
for i in x:
    if i.isalpha():
        l+=chr(27-ord(i))
    else:
        l+=i
print(l)
print(x)
