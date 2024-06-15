pocket = int(input())

if pocket < 0 or pocket > 36:
    print('error')
elif pocket == 0:
    print('green')
elif pocket >= 1 and pocket <= 10 or pocket >= 19 and pocket <= 28:
    if pocket % 2 == 0:
        print('black')
    else:
        print('red')
elif pocket >= 11 and pocket <= 18 or pocket >= 29 and pocket <= 36:
    if pocket % 2 == 0:
        print('red')
    else:
        print('black')

