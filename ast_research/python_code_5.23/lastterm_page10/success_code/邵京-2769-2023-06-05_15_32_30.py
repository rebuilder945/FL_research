str=input()
print(str)
code=[]
for s in str:
    if s.isalpha():
        if s.isupper:
            code.append(chr(155-ord(s)))
        elif s.islower():
            code.append(chr(219-ord(s)))
    else:
        code.append(s)
print(''.join(code))



