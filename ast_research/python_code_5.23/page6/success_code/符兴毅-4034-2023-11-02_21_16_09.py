colour1 = input()
colour2 = input()
primary_color = ['red','blue','yellow']
if colour1 not in primary_color or colour2 not in primary_color or colour1==colour2:
    print('error')
else:
    if colour1==primary_color[0] and colour2==primary_color[1]:
        print('purple')
    elif colour2==primary_color[0] and colour1==primary_color[1]:
        print('purple')
    elif colour2==primary_color[0] and colour1==primary_color[2]:
        print('orange')
    elif colour2==primary_color[2] and colour1==primary_color[0]:
        print('orange')
    elif colour2==primary_color[1] and colour1==primary_color[2]:
        print('green')
    elif colour2==primary_color[2] and colour1==primary_color[1]:
        print('green')
    else:
        print('error')
