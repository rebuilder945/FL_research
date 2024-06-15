a = input()
b = [x for x in a]
c = []
for i in b:
    if i.isalpha():
        if i.islower():
            c1 = ord(i) - 96
            h2 = chr(26-c1+97)
            c.append(h2)
        elif i.isupper():
            h1 = ord(i) - 64
            h3 = chr(26-h1+65)
            c.append(h3)
    else:
        c.append(i)
print("".join(b))
print("".join(c)) 

