a=input()
x=0
y=0
z=0
m=0
for i in a:
    if i.isalpha():
        x+=1
    elif i.isdigit():
        y+=1
    elif i.isspace():
        z+=1
    else:
        m+=1
print(x,z,y,m)
    
