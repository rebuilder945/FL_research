import numbers
zf=input()
yw=0
kg=0
sz=0
qt=len(zf)
for i in zf:
    if i.isalpha():
        yw=yw+1
    elif i.isdigit():
        sz=sz+1
    elif i.isspace():
        kg=kg+1
qt=qt-yw-sz-kg
print(yw,kg,sz,qt,sep=" ")
