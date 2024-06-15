a=input()
b=0
c=0
d=0
f=0
for i in a:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm':
        b+=1
    elif i in '0123456789':
        c+=1
    elif i == ' ':
        d+=1
    else:
        f+=1
print(b,d,c,f)


