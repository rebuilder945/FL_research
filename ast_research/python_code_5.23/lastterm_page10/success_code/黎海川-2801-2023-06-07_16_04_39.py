m=input()
a=list(m)
special_characters = """~!@#$%^&*()_=-/,.?<>;:[]\{\}|\\"""
for i in range(len(a)):
    if "0"<= a[i]<="9":
        n=1
    else:
        n=0
for i in range(len(a)):
    if "a"<=a[i]<="z":
        b=1
    else:
        b=0
for i in range(len(a)):
    if "A"<=a[i]<="Z":
        v=1
    else:
        v=0
if len(a)>=8:
    c=1
else:
    c=0
for i in range(len(a)):
    if a[i] in special_characters:
        x=1
    else:
        x=0
total=x+c+v+b+n
print(total)


