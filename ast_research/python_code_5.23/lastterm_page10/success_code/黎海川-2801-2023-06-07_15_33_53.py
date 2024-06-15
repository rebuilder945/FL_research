m=input()
a=list(m)
for i in range(len(a)):
    if a[i]>=0 and a[i]<="9":
        n=1
    else:
        n=0
    break
for i in range(len(a)):
    if a[i]>="a" and a[i]<="z":
        b=1
    else:
        b=0
    break
for i in range(len(a)):
    if a[i]>="A" and a[i]<="Z":
        v=1
    else:
        v=0
    break
if len(a)>=8:
    c=1
else:
    c=0
for i in range(len(a)):
    if a[i]=='~''!''@''#''$''%''^''&''*''('')''_''=''-''/'',''.''?''<''>'';'':''['']''{''}''|' :
        x=1
    else:
        x=0
    break
total=x+c+v+b+n
print(total)
