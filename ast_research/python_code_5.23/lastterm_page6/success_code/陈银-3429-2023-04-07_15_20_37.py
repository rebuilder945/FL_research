a = input()
b=0
c=0
d=0
e=0
for i in a:
    if 65<=ord(i)<=90 or 97<=ord(i)<=122:
        b+=1
    elif ord(i) == 32:
        c+=1
    elif 48<=ord(i)<=57:
        d+=1
    else:
        e+=1
print(b,c,d,e,end=" ")
