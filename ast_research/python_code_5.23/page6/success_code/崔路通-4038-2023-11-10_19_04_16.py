n=input()
a,b,c,d=0,0,0,0
for i in n:
    if "a"<=i<="z":
        a+=1
    elif"A"<=i<="Z":
        a+=1
    elif "0"<=i<"10":
        b+=1
    elif i==" ":
        c+=1
    else:
        d+=1
print(a,c,b,d)




