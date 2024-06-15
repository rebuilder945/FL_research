c=input()
l=0
s=0
d=0
o=0
for x in c:
    if x.isalpha():
        l=l+1
    elif x.isspace():
        s=s+1
    elif x.isdigit():
        d=d+1
    else:
        o=o+1
print(l,s,d,o)
