x=input()
a=b=c=d=0
for i in x:
    if i in "abcdefghijklmnopqrstuvwxyz" or i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        a=a+1
    elif i ==" ":
        b=b+1
    elif i in "123456789":
        c=c+1
    else:
        d=d+1
print(a,b,c,d)
