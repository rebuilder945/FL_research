import numbers
zf=input()
vw=0
ka=0
sz=0
at=len(zf)
for i in zf:
    if i.isalpha():
        vw=vw+1
    elif i.isdigit():
        sz=sz+1
    elif i.isspace():
        ka=ka+1
at=at-vw-sz-ka
print(vw,ka,sz,at,end=" ")
