a=input()
c=[]
for x in a:
    if  x.isalpha():
        if x.islower():
            i=ord(x)-97
            x=chr(122-i)
            c.append(x)
        else:
            i=ord(x)-65
            x=chr(90-i)
            c.append(x)
    else:
        c.append(x)
print("".join(c))
print(a)



# A-Z 65-90
# a-z 97-122



