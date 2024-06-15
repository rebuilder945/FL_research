
a=input()
b=input()
c=0
for x in a:
    if a.count(x)==b.count(a):
        pass
    else:
        c+=1
for x in b:
    if b.count(x)==a.count(x):
        pass
    else:
        c+=1
if c!=0:
    print("False")
else:
    print("True")





