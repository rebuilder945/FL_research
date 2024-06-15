secondarycolor = ['red','blue','yellow']:
color1=input()
color2=input()
if color1 not in secondarycolor or color2 not in secondarycolor or color1 == color2:
    print('error')
else:
    if color1 == 'red' or color2 == 'red':
        if color1 =='blue' or color2 == 'blue':
            print('purple')
        else:
            print('orange')
    else:
        print('green')

