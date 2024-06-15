secondary_color = (('red','blue','purple'),('red','yellow','orange'),('blue','yellow','green'))
color1 = input()
color2 = input()
primary_color = ('red','blue','green')
if color1 not in primary_color or color2 not in primary_color or color1 == color2:
    print('error')
else:
    for i in secondary_color:
        if color1 in i and color2 in i:
            print(i[2])
