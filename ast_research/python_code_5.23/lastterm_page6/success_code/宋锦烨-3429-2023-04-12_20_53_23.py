str1=input()
a=0
s=0
d=0
o=0
for i in str1:
    if i.isalpha():
        a+=1
    elif i.isspace():
        s+=1
    elif i.isdigit():
        d+=1
    else :
        o+=1
print(a,s,d,o)
