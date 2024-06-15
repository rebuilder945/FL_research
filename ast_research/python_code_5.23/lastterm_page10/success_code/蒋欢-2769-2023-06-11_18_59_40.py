a=input()
print(a)
b=[]
for x in a:
    if x.isalpha():
        if x.isupper():
            n=chr(ord("A")-1+(27-(ord(x)-(ord("A")-1))))
            b.append(n)
        else:
            n=chr(ord("a")-1+(27-(ord(x)-(ord("a")-1))))
            b.append(n)
    else:
        b.append(x)
print("".join(b))
