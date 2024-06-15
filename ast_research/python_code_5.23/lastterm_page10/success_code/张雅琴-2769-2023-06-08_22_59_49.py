a=input()
print(a)
for i in a:
    if i.isalpha():
        if i.isupper():
            print(chr(155-ord(i)),end='')
        elif i.islower():
            print(chr(219-ord(i)),end='')
    else:
        print(i,end='')
