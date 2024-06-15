str=input()
print(str)
for i in str:
    if i.isalpha():
        str.replace(i,chr(155-ord(i)))
print(str)


