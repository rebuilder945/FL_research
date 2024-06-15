ls=list(input())
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0
j=0
for x in ls:
    if ord(x)>=48 and ord(x)<=57:
        a+=1

    if ord(x)>=97 and ord(x)<=122:
        b+=1
    if ord(x)>=65 and ord(x)<=90:
        c+=1
    if (ord(x)>=33 and ord(x)<=47)or (ord(x)>=58 and ord(x)<=64)or(ord(x)>=91 and ord(x)<=96)or(ord(x)>=123 and ord(x)<=126):
        d+=1
    if len(ls)>=8:
        e+=1
if a>0:
    f=1
if b>0:
    g=1
if c>0:
    h=1
if d>0:
    i=1
if e>0:
    j=1
n=f+g+h+i+j
if n==5:
    print('5')
if n==4:
    print('4')
if n==3:
    print('3')
if n==2:
    print("2")
if n==1:
    print('1')
if n==0:
    print('0')    
