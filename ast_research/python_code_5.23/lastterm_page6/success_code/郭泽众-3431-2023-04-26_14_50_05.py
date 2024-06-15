num = int(input())
if 1 <= num <= 36:
    if num % 2 == 0:
        if 1 <= num < 11 or 19 <= num < 29:
            print('black')
        if 11 <= num <= 18 or 29 <= num <= 36:
            print('red')
    else:
        if 1 <= num < 11 or 19 <= num < 29:
            print('red')
        if 11 <= num <= 18 or 29 <= num <= 36:
            print('black')
elif num == 0:
    print('green')
else:
    print('error')
