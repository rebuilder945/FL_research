mima = input()
stars = 0
teshu = "~!@#$%^&*()_=-/,.?<>;:[]{}|\\"


for x in mima:
    if any(x.isdigit()):
        stars += 1
    if any(x.islower()):
        stars += 1
    if any(x.isupper()):
        stars += 1
    if len(mima) >= 8:
        stars += 1
    if any(x in teshu):
        stars += 1

print(stars)
