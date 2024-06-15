c=input()
x=0
for i in c:
    if i.isdigit():
        x+=1
        break
for i in c:
    if i.isupper():
        x+=1
        break
for i in c:
    if i.islower():
        x+=1
        break
if len(c)>=8:
    x+=1
s=" ~!@#$%^&*()_=-/,.?<>;:[]{}|\ "
for i in c:
    if i in s:
        x+=1
        break
print(x)
