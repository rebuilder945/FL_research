x=input()
a=0
b=0
c=0
d=0
for i in x:
    if i.isalpha():
        a+=1
    elif i== " ":
        b+=1
    elif i.isdigit():
        c+=1
    else:
        d+=1
for y in [a,b,c,d]:
    print(y,end=" ")

