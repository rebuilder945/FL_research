import numbers
zf=input()
yw=0
kg=0
sz=0
qt=len(zf)
for i in zf:
    if i.isdigit():
        yw=yw+1
    elif i.isdigit():
        s=sz+1
    elif i.isdigit():
        kg=kg+1
qt=qt-yw-sz-kg
print(yw,kg,sz,qt,end=" ")
