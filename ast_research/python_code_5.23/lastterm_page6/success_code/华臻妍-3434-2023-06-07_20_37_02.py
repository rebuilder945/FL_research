color1=input()
color2=input()
if (color1 and color2 in['red','blue','yellow']) and color1!=color2:
    if (color1=='red' and color2=='blue') or (color2=='red' and color1=='blue'):
        print('purple')
    elif (color1=='red' and color2=='yellow') or (color2=='red' and color1=='yellow'):
        print('orange')
    elif (color1=='blue' and color2=='yellow') or (color2=='blue' and color1=='yellow'):
        print("green")
    else:
        print("error")
else:
    print('error')
