n=list(input())
a=0
b=0
c=0
d=0
for i in n:
    if 65<=ord(i)<=90 or 96<=ord(i)<=122:
        a+=1
    elif 48<=ord(i)<=57:
        b+=1
    elif ord(i)==32:
        c+=1
    else:
        d+=1
print(a,b,c,d,end=" ")
