str=input()
print(str)
for s in str:
    if s.isalpha():
        str.replace(s,chr(155-ord(s)))
print(str)


