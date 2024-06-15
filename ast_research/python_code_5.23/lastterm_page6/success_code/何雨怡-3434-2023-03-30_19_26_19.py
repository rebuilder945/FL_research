color1=input()
color2=input()
if color1==color2:
    print("error")
elif color1 not in ['red','blue','yellow']:
    print("error")
elif color2 not in ['red','blue','yellow']:
    print("error")
else:
    if color1=='red' and color2=='blue':
        print("purple")
    elif color1=='blue' and color2=='red':
        print('purple')
    elif color1=='red' and color2=='yellow':
        print('orange')
    elif color1=='yellow' and color2=='red':
        print('orange')
    elif color1=='blue' and color2=='yellow':
        print('green')
    elif color1=='yellow' and color2=='blue':
        print('green')
    else:
        pass
