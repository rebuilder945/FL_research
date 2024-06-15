s=input()
star=0
for i1 in s:
    if i1.isupper():
        star+=1
        break
for i2 in s:
    if i2.islower():
        star+=1
        break
for i3 in s:
    if i3.isdigit():
        star+=1
        break
for i4 in s:
    if i4 in '~!@#$\\%^&*()_={-/,.?<>;:[]}|':
        star+=1
        break
if len(s)>=8:
    star+=1
print(star)
