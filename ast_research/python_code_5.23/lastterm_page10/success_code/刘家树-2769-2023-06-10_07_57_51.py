a1=input()
a="".join(list(a1))
for x in a:
    if x.isalpha() and x in "abcdefghijklmnopqrstuvwxyz":
        a=a.replace(x,chr(ord("a")+ord("z")-ord(x)))
    elif x.isalpha() and x in "abcdefghijklmnopqrstuvwxyz".upper():
        a=a.replace(x,chr(ord("A")+ord("Z")-ord(x)))
    else:
        pass
print(a1)
print(a)

