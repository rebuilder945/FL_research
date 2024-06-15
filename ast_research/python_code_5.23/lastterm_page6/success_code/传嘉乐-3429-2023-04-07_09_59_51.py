s=input()
a=0
b=0
c=0
d=0
for x in s:
    if x.isalpha():
        a+=1
    elif x.isspace():
        b+=1
    elif x.isdigit():
        c+=1
    else:
        d+=1
print(a,b,c,d)
