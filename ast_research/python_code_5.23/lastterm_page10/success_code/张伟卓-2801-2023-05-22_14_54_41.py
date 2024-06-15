


cod=input()
star=0
for i in cod:
    if i.isalnum:
        star+=1
        break
for i in cod:
    if i.isupper:
        star+=1
        break
for i in cod:
    if i.islower:
        star+=1
        break
for i in cod:
    if len(cod)>=8:
        star+=1
        break
for i in cod:
    if i in ["~!@#$%^&*()_=-/,.?<>;:|"]:
        star+=1
        break
print(star)


