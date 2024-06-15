


cod=input()
star=0
for i in cod:
    if i.isalnum:
        star+=1
        break
    elif i.isupper:
        star+=1
        break
    elif i.islower:
        star+=1
        break
    elif len(cod)>=8:
        star+=1
        break
    elif i in ["~!@#$%^&*()_=-/,.?<>;:|"]:
        star+=1
        break
print(star)


