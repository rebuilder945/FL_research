strname=input()
a=0
b=0
c=0
d=0
for i in strname:
    if i.isalpha():
        a+=1
    elif i.isspace():
        b+=1
    elif i.isdigit():
        c+=1
    else:
        d+=1
print(a,b,c,d)
