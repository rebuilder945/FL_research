n=input()
a=0
b=0
c=0
d=0
e='0123456789'
f='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
for i in n:
    if i in f:
        a=a+1
    elif i==" ":
        b=b+1
    elif i in e:
        c=c+1
    else:
        d=d+1
print(a,b,c,d)

