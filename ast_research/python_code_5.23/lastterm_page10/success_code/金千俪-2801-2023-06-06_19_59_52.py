a=input()
x=0
y=0
z=0
q=0
w=0
for i in a :
    if "1"<=i<="9":
        x=1
for i in a :
    if"a"<=i<="z":
        y=1
for i in a :
    if "A"<=i<="Z":
        z=1  
for i in a :
    if i in "~!@#$%^&*()_=-/,.?<>;:[]{}|\]":
        q=1
if len(a)>=8:
        w=1
print(x+y+z+q+w)

