from turtle import color


color1=input()
color2=input()
if color1!="red" and color1!="blue"and color1!="yellow"or color1==color2:
    print("error")
elif color1+color2=="red,blue":
    print("purple")
elif color1+color2=="red,yellow":
    print("orange")
elif color1+color2=="yellow,blue":
    print("green")

