a=input()
b=0
c=0
d=0
e=0
f=[]
for i in range(len(a)):
    if a[i] in "qwertyuiopasdfghjklzxcvbnmQWASEDRFTGYHUJIKOLPZXCVVBNM":
        b=b+1
    elif a[i]==" ":
        c=c+1
    elif a[i] in "1234567890":
        d=d+1
    else:
        e=e+1
print(b,c,d,e)
