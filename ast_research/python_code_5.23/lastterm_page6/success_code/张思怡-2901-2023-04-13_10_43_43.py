sumd=0
n=0
m=1
while m:
    a=input()
    if (a!="#"):
        n+=1
        sumd+=int(a)
    else:
        m=0
print(n,sumd)
