stext=input()
final=""
for i in stext:
    if i.islower():
        final+=(chr(219-ord(i)))
    elif i.isupper():
        final+=(chr(155-ord(i)))
    else:    
        final+=i
print(stext)
print(final)
