n=input()
a,b,c,d=0,0,0,0
for i in n:
    if i.isalpha():
        a+=1
    elif i.isspace():
        b+=1
    elif i.isdigit():
        c+=1
    else:
        d+=1
print(a,b,c,d)
