a=input()
print(a)
for x in a:
    if x.isalpha():
        if x.isupper():
            b=x.lower()
            b=chr(ord('a')+(26-(ord(b)-ord('a'))-1))
            b=b.upper()
            print(b,end='')
        else:
            x=chr(ord('a')+(26-(ord(x)-ord('a'))-1))
            print(x,end='')
    else:
        print(x,end='')
