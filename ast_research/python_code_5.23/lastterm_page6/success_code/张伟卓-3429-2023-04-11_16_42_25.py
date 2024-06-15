x=input()
c=0
s=0
n=0
o=0
for i in x:
    if i.isalpha():
        c+=1
    elif i.isdigit():
        n+=1
    elif i.isspace():
        s+=1
    else:
        o+=1
print(c,s,n,o)
