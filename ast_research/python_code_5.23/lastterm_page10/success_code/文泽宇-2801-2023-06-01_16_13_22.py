n=input()
lst=[i for i in n]
c=0
fuhao="~!@#$%^&*()_=-/,.?<>;:[]{|}\\"
fu=[d for d in fuhao]
if len(n)>8:
    c=1
for x in lst:
    if x.isupper():
        c+=1
        break
for x in lst:
    if x.islower():
        c+=1
        break
for x in lst:
    if x.isdecimal():
        c+=1
        break
for x in lst:
    if x in fuhao:
        c+=1
        break
print(c)

