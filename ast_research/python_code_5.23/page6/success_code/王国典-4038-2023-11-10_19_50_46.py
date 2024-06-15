s=input()
a,b,c,d=0,0,0,0
for i in s:
    if "a"<=i<="z":
        a+=1
    if i==" ":
        b+=1
    if "0"<=i<="9":
        c+=1
    else:
        d+=1
print(a,b,c,d)
