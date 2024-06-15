a=input()
b='~!@#$%^&*()_=-/,.?<>;:[]{}|\\'
c=0
if len(a)>=8:
    c+=1
for i in a:
    if i.isdigit():
        c+=1
    for x in a:
        if x.isdigit():
            a=a.replace(x,'')
    break
for i in a:
    if i.islower():
        c+=1
    for x in a:
        if x.islower():
            a=a.replace(x,'')
    break
for i in a:
    if i.isupper():
        c+=1
    for x in a:
        if x.isupper():
            a=a.replace(x,'')
    break  
for i in a:
    if i in b:
        c+=1
    for x in a:
        if x in b:
            a=a.replace(x,'')
print(c)



