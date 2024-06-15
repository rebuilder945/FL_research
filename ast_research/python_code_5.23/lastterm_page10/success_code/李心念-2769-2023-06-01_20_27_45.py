s = input()
print(s)
for x in s:
    if x.isalpha():
        if x.istitle:
            print(chr(123-(98-ord(x.lower())).upper()),end='')
        else:
            print(chr(123-(98-ord(x))),end='')
    else:
        print(x,edn='')
