n=input()
lst=list(n)
a=0
b=0
c=0
d=0
for i in range(len(lst)):
    if (ord(lst[i])>=65 and ord(lst(i))<=90) or (ord(lst[i])>=97 and ord(lst(i))<=122):
        a=a+1
    elif lst[i]==" ":
        b=b+1
    elif ord(lst[i])>=48 and ord(lst[i])<=57:
        c=c+1
    else:
        d=d+1
print("{} {} {} {}".format(a,b,c,d))

