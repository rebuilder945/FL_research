a=input()
print(a)
b=""
for i in a:
    if i.islower():
        b=b+chr(ord("a")+(ord("z")-ord(i)))
    elif i.isupper():
        b=b+chr(ord("A")+(ord("Z")-ord(i)))
    else:
        b=b+i
print(b)




