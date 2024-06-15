star = 0
ls = input()
for x in ls:
    if "0"<=x<="9":
        star+=1
        break
for x in ls:
    if "a"<=x<="z":
        star+=1
        break
for x in ls:
    if "A"<=x<="Z":
        star+=1
        break
for x in ls:
    if x in "~!@#$%^&*()_=-/,.?<>;:[]{}\|":
        star+=1
        break
if len(ls) >=8:
    star+=1
else:
    star+=0
print(star)




