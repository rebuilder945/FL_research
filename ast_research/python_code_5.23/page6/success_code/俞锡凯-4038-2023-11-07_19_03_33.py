a=input()
b,c,d,e=0,0,0,0
for i in a:
    if i.isalpha():
        b+=1
    elif i.isspace():
        c+=1
    elif i.isdigit():
        d+=1
    else:
        e+=1
print(b,c,d,e)
