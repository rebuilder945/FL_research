primarycolor=['red','blue','yellow']
color1=input()
color2=input()
if color1==color2 or color1 not in primarycolor or color2 not in primarycolor:
    print('error')
else:
    if color1=='rad':
        if color2=='blue':
            print('purple')
        else:
            print('orange')
    else:
        print('green')
