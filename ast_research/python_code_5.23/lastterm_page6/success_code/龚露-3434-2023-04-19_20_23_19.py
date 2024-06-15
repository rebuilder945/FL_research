color1 = input()
color2 = input()
if color1!=color2:
    if [color1,color2] in ['red','blue'] or ['blue','red']:
        print('purple')
    elif [color1,color2] in ['red','yellow'] or ['yellow','red']:
        print('orange')
    elif [color1,color2] in ['blue','yellow'] or ['yellow','blue']:
        print('green')
    else:
        print('error')
else:
    print('error')

