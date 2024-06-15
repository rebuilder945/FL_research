a=input()
star=0
ls="\~!@#$%^&*()_=-/,.?<>;:[]{}|+"
for i in a:
    if i.isnumeric():
        star+=1
        break
for i in a:    
    if i.islower():
        star+=1
        break
for i in a:   
    if i.isupper():
        star+=1
        break
if len(a)>=8:
    star+=1
for i in a:
    if i in ls :
        star+=1
        break

print(star)
