a=input()
l=0
s=0
d=0
o=0
for i in a:
    if i.isalpha():
        l+=1
    elif i.isspace():
        s+=1
    elif i.isdigit():
        d+=1
    else:
        o+=1
print(l,s,d,o)
