a = input("")

b = set(a)
c = {}

for i in b:
    if i.isalpha():
        c[i] = a.count(i)

if c == {}:
    print("no alpha")

else:
    max1 = max(c.values())

    data = list(c.items())

    data.sort()

    for i in data:
        if i[1] == max1:
            print(i[0], i[1])

