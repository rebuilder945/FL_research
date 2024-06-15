color1 = input()
color2 = input()
primary_color = ["red","yellow","blue"]
if color1 == color2 or color1 not in primary_color or color2 not in primary_color:
    print("error")
else:
    if color1 == primary_color[0] and color2 == primary_color[1] or color1 == primary_color[1] and color2 == primary_color[0]:
        print("orange")
    if color1 == primary_color[0] and color2 == primary_color[2] or color1 == primary_color[2] and color2 == primary_color[0]:
        print("purple")
    if color1 == primary_color[1] and color2 == primary_color[2] or color1 == primary_color[2] and color2 == primary_color[1]:
        print("green")
