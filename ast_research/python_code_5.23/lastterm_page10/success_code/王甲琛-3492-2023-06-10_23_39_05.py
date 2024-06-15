str0 = input()
for it in str0:
    number = str0.count(it)
    if number == 1:
        print(it)
        break
else:
    print(None)

