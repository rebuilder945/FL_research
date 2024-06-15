code=input()
lst=list(code)
lst2=[]
for x in lst:
    if x.isalpha():
        if x.islower():
            x=chr((25-(int(ord(x))-int(ord('a'))))+int(ord('a')))
            lst2.append(x)
        else:
            x=chr((25-(int(ord(x))-int(ord('A'))))+int(ord('A')))
            lst2.append(x)
    else:
        lst2.append(x)
print(code)
print(''.join(lst2))
