a=input()
yw=0
kg=0
sz=0
qt=0
for i in a:
    if i.isalpha():
        yw+=1
    elif i.isspace():
        kg+=1
    elif i.isdigit():
        sz+=1
    else:
        qt+=1
print(yw,kg,sz,qt)

