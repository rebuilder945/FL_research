m=input()

for i in range(len(m)):
    if i>="0" and i<="9":
        n=1
    else:
        n=0
    break
for i in range(len(m)):
    if i>="a" and i<="z":
        b=1
    else:
        b=0
    break
for i in range(len(m)):
    if i>="A" and i<="Z":
        v=1
    else:
        v=0
    break
if len(m)>=8:
    c=1
else:
    c=0
for i in range(len(m)):
    if i=='~''!''@''#''$''%''^''&''*''('')''_''=''-''/'',''.''?''<''>'';'':''['']''{''}''|' :
        x=1
    else:
        x=0
    break
total=x+c+v+b+n
print(total)
