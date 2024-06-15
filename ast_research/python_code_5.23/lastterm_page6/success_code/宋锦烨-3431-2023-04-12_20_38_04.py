a=int(input())
if a == 0:
    print(green)
elif a<=10:
    if a%2 == 1:
        print(red)
    else:
        print(black)
elif a<=18:
    if a%2 == 1:
        print(black)
    else:
        print(red)
elif a<=28:
    if a%2 == 1:
        print(red)
    else:
        print(black)
elif a<=36:
    if a%2 == 1:
        print(black)
    else:
        print(red)
else:
    print(error)
