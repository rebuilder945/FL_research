n=input().split()
s=0
b=0
d=0
o=0
for i in n:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        s+=1
    elif i.isspace():
        b+=1
    else:
        o=o+1
print(s,b,d,o)

