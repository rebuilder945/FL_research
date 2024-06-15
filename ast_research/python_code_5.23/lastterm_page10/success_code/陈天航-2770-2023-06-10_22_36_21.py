a=input()
b=len(a)
c,d,e,f,g=0,0,0,0,0
h="~!@#$%^&*()_=-/,.?<>;:[]{}|\\"
if b>=8:
    c=1
for i in a:
    if i.isupper():
        d=1
    elif i.islower():
        e=1
    elif i.isdigit():
        f=1
    elif i in h:
        g=1
print(c+d+e+f+g)
    

