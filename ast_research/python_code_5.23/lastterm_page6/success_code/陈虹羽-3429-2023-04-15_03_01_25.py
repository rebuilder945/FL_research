a=input()
b=0
c=0
d=0
e=0
for i in a:
    if i.isdigit():
        b+=1
    elif i.isspace():
        c+=1
    elif i.isalpha():
        d+=1
    else:
        e+=1
print(d,c,b,e)

