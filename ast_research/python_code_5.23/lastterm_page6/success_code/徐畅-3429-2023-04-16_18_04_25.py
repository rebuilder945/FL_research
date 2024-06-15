n=input()
lst=list(n)
a=0
b=0
c=0
d=0
for i in range(len(lst)):
    if lst[i]in [chr(n) for n in range(97,123) and range(65,90)]:
        a=a+1
    elif lst[i]==" ":
        b=b+1
    elif ord(lst[i])>=48 and ord(lst[i])<=57:
        c=c+1
    else:
        d=d+1
print("{} {} {} {}".format(a,b,c,d))

