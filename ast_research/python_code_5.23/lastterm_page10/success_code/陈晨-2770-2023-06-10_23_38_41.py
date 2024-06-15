s1=input()
s2=input()
ls1,ls2=list(s1),list(s2)
r=0
for x in ls1:
    if x in ls2:
        if ls1.count(x)==ls2.count(x):
            r+=0
        else:r+=1
    else:
        r+=1
if r==0:
    print("True")
else:
    print("False")

