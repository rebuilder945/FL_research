a=input()
b=[0,0,0,0,0]
for i in a:
    if type(eval(i))==int:
        b[0]=1
    elif "a"<=i<="z":
        b[1]=1
    elif "A"<=i<="Z":
        b[2]=1
    elif i in " ~!@#$%^&*()_=-/,.?<>;:[]{|}\ ":
        b[4]=1
if len(a)>=8:
        b[3]=1
print(sum(b))
    
