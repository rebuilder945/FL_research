s = input()
a,b,c,d = 0,0,0,0
for i in s:
    if "a"<=i<="z" or "A"<=i<="Z":
        a += 1
    elif i == ' ':
        b+=1
    elif "0" <= i <="9":
        c+=1
    else:
        d+=1
print(a,b,c,d)

