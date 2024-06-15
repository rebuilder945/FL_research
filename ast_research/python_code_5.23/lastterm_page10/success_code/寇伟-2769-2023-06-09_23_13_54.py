password = input()
ls = list(password)
for i in range(len(password)):
    if ls[i].isalpha():
        ls[i]=chr(2*ord('a')-ord(ls[i])+25)
print(password)
print(''.join(ls))

