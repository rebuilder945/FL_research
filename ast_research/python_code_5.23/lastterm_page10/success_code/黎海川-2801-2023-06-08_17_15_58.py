m=input()
special_characters = """~!@#$%^&*()_=-/,.?<>;:[]\{\}|\\"""
result = [0, 0, 0, 0,0]
for i in m:
    if "0"<= i <="9":
        result[0]=1
    elif i.isupper():
        result[1]=1
    elif i.islower():
        result[2]=1
    elif i in special_characters:
        result[3]=1
if len(m)>=8:
    result[4]=1

print(result.count(1))




