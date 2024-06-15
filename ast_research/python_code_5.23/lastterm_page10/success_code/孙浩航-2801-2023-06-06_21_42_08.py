a=input()
b=[0,0,0,0,0]
for x in a:
    if "0"<=x<="9":
        b[0]=1
    elif "a"<=x<="z":
        b[1]=1
    elif "A"<=x<="Z":
        b[2]=1
    elif x in "~!@#$%^&*()_=-/,.?<>;:[]{}|\\":
        b[3]=1
if len(a)>=8:
    b[4]=1
print(b.count(1))

    

