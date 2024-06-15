color1=input()
color2=input()
s1={color1,color2}
purple={"red","blue"}
orange={"red","yellow"}
green={"blue","yellow"}
total={"blue","yellow","red"}
if color1 not in total or color2 not in total or color1==color2:
    print("error")
elif s1==purple:
    print("purple")
elif s1==orange:
    print("orange")
else:
    print("green")
