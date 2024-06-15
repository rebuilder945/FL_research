a=input()
z=0
d="~!@#$%^&*()_=-/,.?<>;:[]{}\|"
e="abcdefghijklmnopqrstuvwxyz"
f="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in a :
    if i.isdigit():
        z+=1
        break
for i in a:
    if i in d:
        z+=1
        break
for i in a:
    if i in e:
        z+=1
        break
for i in a:
    if i in f:
        z+=1
        break
if len(a)>=8:
    z+=1
print(z)
