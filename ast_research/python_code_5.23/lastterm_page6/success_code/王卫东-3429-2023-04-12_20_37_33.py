n=list(input())
a=0
b=0
c=0
d=0
for x in n:
    if (ord(x)>=65 and ord(x)<=90) or (ord(x)>=97 and ord(x)<=122):
        a+=1
    elif ord(x)>=48 and ord(x)<=57:
        b+=1
    elif str(x)==' ':
        c+=1
    else:
        d+=1
print(a,c,b,d)                     
