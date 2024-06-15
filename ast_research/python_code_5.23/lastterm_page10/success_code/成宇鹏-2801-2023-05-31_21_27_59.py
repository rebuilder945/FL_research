from turtle import st


s = input()
star = 0
a =[]
b= []
c =[]
d =[]

if len(s) <= 28:
    for x in s:
        if x.isalpha():
            if x.isupper():
                a.append(x)
            elif x.islower():
                b.append(x)
        elif x.isnumeric():
            c.append(x)
        else:
            d.append(x)
    for i in [a,b,c,d]:
        if i != []:
            star += 1
    if len(s)>= 8:
        star += 1
print(star)

