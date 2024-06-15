color1=input()
color2=input()
s1={color1,color2}
purpleset={"red","blue"}
orangeset={"red","yellow"}
tricolor={"red","blue","yellow"}
if color1 not in tricolor or color2 not in tricolor or color1==color2:
    print("error")
elif s1 in purpleset:
    print("purple")
elif s1 in orangeset:
    print("orange")
else:
    print("green")

