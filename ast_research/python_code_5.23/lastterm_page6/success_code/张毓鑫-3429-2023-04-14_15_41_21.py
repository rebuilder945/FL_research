a=input()
b=0
c=0
d=0
e=0
for i in a:
    if i.isalpha():
        b+=1
    elif i ==' ':
        c+=1
    elif i.isdigit():
        d+=1
    else:
        e+=1
print(b,c,d,e)
