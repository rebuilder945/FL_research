s=input()
print(s)
for i in s:
    if i.isalpha():
        if i.isupper():
            i=chr(64+64+26-ord(i)+1)
            print(i,end='')
        else:
            i=chr(96+96+26-ord(i)+1)
            print(i,end='')
    else:
        print(i,end='')
