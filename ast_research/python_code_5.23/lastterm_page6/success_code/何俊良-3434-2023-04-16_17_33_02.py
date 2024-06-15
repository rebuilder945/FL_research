colors = {'red': ['purple', 'orange'], 'blue': ['purple', 'green'], 'yellow': ['green', 'orange']}

color1 = input().strip().lower()
color2 = input().strip().lower()

if color1 == color2 or color1 not in colors.keys() or color2 not in colors.keys():
    print('error')
else:
    print(colors[color1][0] if color2 == list(filter(lambda c: c != color1, colors.keys()))[0] else colors[color1][1])

