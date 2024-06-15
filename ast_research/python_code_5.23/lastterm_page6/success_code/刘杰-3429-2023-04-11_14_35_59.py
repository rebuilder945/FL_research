lst=list(input())
a=0
b=0
c=0           
d=0
for i in lst:
    if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        a+=1
    elif i==' ':
        b+=1
    elif ord(i)>=48 and ord(i)<=57:
        c+=1
    else:
        d+=1
print(a,b,c,d,end=' ')
