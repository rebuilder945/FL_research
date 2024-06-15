def colormix(color1,color2):
    if color1==ls[0]:
        if color2==ls[1]:
            return "purple"
        else:
            return "orange"
    elif color1==ls[1]:
        if color2==ls[0]:
            return "purple"
        else:
            return "green"
    else:
        if color2==ls[0]:
            return "orange"
        else:
            return "green"

color1=input()
color2=input()
ls=[red,blue,yellow]
if color1==color2:
    print("error")
elif color1 not in ls or color2 not in ls:
    print("error")
else:
    colormix(color1,color2)
    print(colormix)
