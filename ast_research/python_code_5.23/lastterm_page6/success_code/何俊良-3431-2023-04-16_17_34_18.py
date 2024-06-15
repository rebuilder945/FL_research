number = input().strip()

if not number.isdigit():
    print('error')
else:
    number = int(number)
    if number < 0 or number > 36:
        print('error')
    elif number == 0:
        print('green')
    elif number >= 1 and number <= 10 or number >= 19 and number <= 28:
        print('red' if number % 2 == 1 else 'black')
    else:
        print('black' if number % 2 == 1 else 'red')

