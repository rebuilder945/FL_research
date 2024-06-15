n="~!@#$%^&*()=-/,.?<>;[]{}\|"
da="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
xiao="abcdefghijklmnopqrstuvwxyz"
shu="1234567890"
da1=0
xiao1=0
shu1=0
zi1=0
password=input()
du=0
if len(password)>=8:
    du+=1
for i in password:
    if i in shu:
        shu1+=1
    elif i in xiao:
        xiao1+=1
    elif i in da:
        da1+=1
    elif i in n:
        zi1+=1
if shu1>0:
    du+=1
if xiao1>0:
    du+=1
if da1>0:
    du+=1
if zi1>0:
    du+=1
print(du)

