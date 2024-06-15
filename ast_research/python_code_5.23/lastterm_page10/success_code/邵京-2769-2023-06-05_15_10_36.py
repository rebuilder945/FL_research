str=input()
str1=str
for i in str1:
    if i.isalpha():
        str1.replace(i,chr(155-ord(i)),1)
print(str)
print(str1)


