str=input()
print(str)
code=[]
for i in str:
    if i.isalpha():
        if i.isupper():
            code.append(chr(155-ord(i)))
        elif i.islower():
            code.append(chr(219-ord(i)))
    else:
        code.append(i)
print(''.join(code))
