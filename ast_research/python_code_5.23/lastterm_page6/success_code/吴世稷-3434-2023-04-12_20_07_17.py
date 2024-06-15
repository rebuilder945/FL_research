pri_color1 = input()
pri_color2 = input()
if pri_color1 != pri_color2:
    if pri_color1 == 'red' and pri_color2 == 'blue':
        print('purple')
    elif pri_color1 == 'bule' and pri_color2 == 'red':
        print('purple')
    elif pri_color1 == 'red' and pri_color2 == 'yellow':
        print('orange')
    elif pri_color1 == 'yellow' and pri_color2 == 'red':
        print('orange')
    elif pri_color1 == 'blue' and pri_color2 == 'yellow':
        print('green')
    elif pri_color1 == 'yellow' and pri_color2 == 'blue':
        print('green')
    else:
        print('error')

