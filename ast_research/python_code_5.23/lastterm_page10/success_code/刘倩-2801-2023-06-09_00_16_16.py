mima = input()
stars = 0
teshu = "~!@#$%^&*()_=-/,.?<>;:[\]{\}|\\"


for x in mima:
    if x.isdigit():
        stars += 1
    if x.islower():
        stars += 1
    if x.isupper():
        stars += 1
    if len(mima) >= 8:
        stars += 1
    if x in teshu:
        stars += 1

print(stars)
