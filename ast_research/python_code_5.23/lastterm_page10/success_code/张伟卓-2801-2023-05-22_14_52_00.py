


cod=input()
star=0
for i in cod:
    if i.isalnum:
        star+=1
        continue
    elif i.isupper:
        star+=1
        continue
    elif i.islower:
        star+=1
        continue
    elif len(cod)>=8:
        star+=1
        continue
    elif i in ["~!@#$%^&*()_=-/,.?<>;:|"]:
        star+=1
        continue
print(star)


