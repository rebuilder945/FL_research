color1 = input().lower()
color2 = input().lower()

if color1 not in ['red', 'blue', 'yellow'] or color2 not in ['red', 'blue', 'yellow']:
    print('error')
elif color1 == color2:
    print('error')
else:
    if (color1 == 'red' and color2 == 'blue') or (color1 == 'blue' and color2 == 'red'):
        print('purple')
    elif (color1 == 'red' and color2 == 'yellow') or (color1 == 'yellow' and color2 == 'red'):
        print('orange')
    elif (color1 == 'blue' and color2 == 'yellow') or (color1 == 'yellow' and color2 == 'blue'):
        print('green')

