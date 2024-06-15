n=input()
a=0
shuzi=0
xiaoxie=0
daxie=0
changdu=0
zifu=0
ls1="\~!@#$%^&*()_=-/,.?<>;:[]}{|"
for x in n:
    if type(x)==int or float:
        shuzi+=1
        if shuzi>0:
            a+=1
    elif ord(x) in range(65,91):
        xiaoxie+=1
        if xiaoxie>0:
            a+=1
    elif ord(x) in range(97,123):
        daxie+=1
        if daxie>0:
            a+=0
    elif x in ls1:
        zifu+=1
        if zifu>0:
            a+=1
if len(n)>=8:
    a+=1
print(a)
