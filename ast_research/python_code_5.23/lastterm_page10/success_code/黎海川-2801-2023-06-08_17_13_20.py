m=input()
special_characters = """~!@#$%^&*()_=-/,.?<>;:[]\{\}|\\"""
for i in m:
    if "0"<= i <="9":
        n=1
    elif i.isupper():
        b=1
    elif i.islower():
        v=1
    elif i in special_characters:
        f=1
if len(m)>=8:
    c=1
else:
    c=0
total=f+c+v+b+n
print(total)




