a=input()
b,c,d,e=0,0,0,0
for i in a:
    if "a"<=i<="z" or "A"<=i<="Z":
        b+=1
    elif "0"<=i<="9":
        d+=1
    elif i==" ":
        c+=1
    else:
        e+=1
print(b,c,d,e)

