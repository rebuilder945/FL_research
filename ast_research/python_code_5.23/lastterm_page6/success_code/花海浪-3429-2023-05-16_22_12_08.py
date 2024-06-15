str=input()
a=0
b=0
c=0
d=0
for i in str:
    if "a"<=i<="z"or "A"<=i<="Z":
        a+=1
    elif i==" ":
        b+=0
    elif "0"<=i<="9":
        c+=1
    else:
        d+=1
print("%d %d %d %d"%(a,b,c,d))

