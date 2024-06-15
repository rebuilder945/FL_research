a=input()
for x in a:
    if  x.isalpha():
        if x.islower():
            i=ord(x)-97
            print(chr(122-i),end='')
        else:
            i=ord(x)-65
            print(chr(90-i),end='')
    else:
        print(x,end='')
print(a)


# A-Z 65-90
# a-z 97-122



