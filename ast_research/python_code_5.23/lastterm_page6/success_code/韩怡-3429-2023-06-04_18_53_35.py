s=input()
a=b=c=d=0
m="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
n="1234567890"
for i in s:
    if i in m:
        a+=1
    elif i in [""]:
        b+=1
    elif i in n:
        c+=1
    else:
        d+=1
print(a,b,c,d)

