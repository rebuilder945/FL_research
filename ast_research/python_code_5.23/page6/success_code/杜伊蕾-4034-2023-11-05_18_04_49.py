color1 = input("")
color2 = input("")

if color1 in ['red', 'blue', 'yellow'] and color2 in ['red', 'blue', 'yellow'] and color1 != color2:
    if (color1 == 'red' and color2 == 'blue') or (color1 == 'blue' and color2 == 'red'):
        print("紫色")
    elif (color1 == 'red' and color2 == 'yellow') or (color1 == 'yellow' and color2 == 'red'):
        print("橙色")
    elif (color1 == 'blue' and color2 == 'yellow') or (color1 == 'yellow' and color2 == 'blue'):
        print("绿色")
else:
    print("error")
