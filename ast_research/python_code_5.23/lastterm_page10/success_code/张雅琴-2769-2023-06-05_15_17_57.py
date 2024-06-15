s=input()
print(s)
for i in s:
    if i.isalpha():
        if i.isupper():
            print(chr(155-ord(i)),end="")
        else:
            print(chr(219-ord(i)),end="")
    else:
        print(i,end="")
