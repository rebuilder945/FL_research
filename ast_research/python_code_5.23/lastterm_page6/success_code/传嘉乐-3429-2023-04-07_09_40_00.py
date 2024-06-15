s=input()
a=0
b=0
c=0
d=0
for x in s:
    if type(x)==type(a):
        a+=1
    elif type(x)==type(" "):
        b+=1
    elif type(x)==type(1):
        c+=1
    else:
        d+=1
print(a,b,c,d)
