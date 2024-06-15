a=input()
k=''
c=list('abcdefghijklmnopqrstuvwxyz')
d=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for i in range(0,len(a)):
    if not str.isalpha (a[i]):
        k=k+a[i]
    else:
        if ord(a[i])>=65 and ord(a[i])<=90:
            b=chr(122+65-ord(a[i]))
            if b in c:
                b=d[c.index(b)]
            else:
                b=c[d.index(b)]
            k=k+b
        else:
            b=chr(65+122-ord(a[i]))
            if b in c:
                b=d[c.index(b)]
            else:
                b=c[d.index(b)]
            k=k+b
print(k)
