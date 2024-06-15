a=input()
b=0
c=0
d=0
e=0
for i in a:
    if type(i)==type("a"):
        b+=1
    elif i.isspace():
        c+=1
    elif type(i)==type(1):
        d+=1
    else:
        e+=1
print(b,c,d,e)
        

