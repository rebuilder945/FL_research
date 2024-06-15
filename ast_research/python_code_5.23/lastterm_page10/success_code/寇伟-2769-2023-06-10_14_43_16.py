password = input()
ls = list(password)
for i in range(len(password)):
    if ls[i].isalpha():
        if ls[i].isupper():
            ls[i]=ls[i].lower()
            ls[i]=chr(2*ord('a')-ord(ls[i])+25)
            ls[i]=ls[i].upper()
        else:
            ls[i]=chr(2*ord('a')-ord(ls[i])+25)
print(password)
print(''.join(ls))

