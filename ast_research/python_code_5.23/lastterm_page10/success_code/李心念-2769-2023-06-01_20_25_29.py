s = input()
print(s)
for x in s:
    if x.isalpha():
        print(chr(123-(98-ord(x))),end='')
    else:
        print(x,edn='')
