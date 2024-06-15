color1=input()
color2=input()
pcolor=["red","blue","yellow"]
purple=["red","blue"]
orange=["red","yellow"]
green=["blue","yellow"]
if color1==color2:
    print("error")
elif color1 not in pcolor or color2 not in pcolor:
    print("error")
else:
    if color1 in purple and color2 in purple:
        print("purple")
    elif color1 in orange and color2 in orange:
        print("orange")
    else:
        print("green")

