color1=input()
color2=input()
purple={"red","blue"}
orange={"red","yellow"}
green={"blue","yellow"}
if color1==color2:
    print("error")
elif color1!=color2 and color1 in purple and color2 in purple:
    print("purple")
elif color1!=color2 and color1 in orange and color2 in orange:
    print("orange")
elif color1!=color2 and color1 in green and color2 in green:
    print("green")
else:
    print("error")


