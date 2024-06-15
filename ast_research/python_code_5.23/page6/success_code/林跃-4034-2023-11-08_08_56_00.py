color1=input()
color2=input()
c1={color1,color2}
purpleset={"red","blue"}
greenset={"blue","yellow"}
orangeset={"red","yellow"}
colorset={"red","blue","yellow"}
if color1==color2 or color1 not in colorset or color1 not in colorset:
    print("error")
elif c1==purpleset:
    print("purple")
elif c1==greenset:
    print("green")
else:
    print("orange")
