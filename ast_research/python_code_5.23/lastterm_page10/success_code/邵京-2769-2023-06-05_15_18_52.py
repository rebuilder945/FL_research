str=input()
print(str)
for i in range(len(str)):
    if str[i].isalpha():
        str[i]=chr(155-ord(str[i]))
print(str)


