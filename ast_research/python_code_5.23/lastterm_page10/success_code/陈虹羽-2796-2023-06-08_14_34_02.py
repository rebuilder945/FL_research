print(a=input())
b=''
c=0
d=''
ma=0
for i in a:
    if i.isdigit():
        b+=i
        c+=1
    else:
        if c>=ma:
            ma=c
            d=b
            b=''
            c=0
        else:
            b=''
            c=0
if b!='':
    if c>=ma:
        ma=c
        d=b
    print(d)
if d=='':
    print('No digits')



