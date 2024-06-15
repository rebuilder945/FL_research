n=input()
lst=list(n)
a=0
b=0
c=0
d=0
for i in lst:
    if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        a=a+1
    elif i==" ":
        b=b+1
    elif ord(i)>=48 and ord(i)<=57:
        c=c+1
    else:
        d=d+1
print("{} {} {} {}".format(a,b,c,d))

