m=input()
special_characters = """~!@#$%^&*()_=-/,.?<>;:[]\{\}|\\"""
for i in m:
    if "0"<= i <="9":
        n=1
    else:
        n=0
for i in m:
    if i.isupper():
        b=1
    else:
        b=0
for i in m:
    if i.islower():
        v=1
    else:
        v=0
if len(m)>=8:
    c=1
else:
    c=0
for i in m:
    if i in special_characters:
        x=1
    else:
        x=0
total=x+c+v+b+n
print(total)




