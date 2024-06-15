sstr=input()
a=0
b=0
c=0
for i in sstr:
    if "a"<=i<='z'or "A"<=i<="Z":
        a+=1
    elif i==" ":
        b+=1
    elif "1"<=i<="9":
        c+=1
d=len(sstr)-a-b-c
print(a,b,c,d)

