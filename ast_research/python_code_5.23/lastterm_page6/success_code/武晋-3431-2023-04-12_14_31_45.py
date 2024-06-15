color1 = input()
color2 = input()
s1={color1,color2}
purpleset={"red","blue"}
orangeset={"red","yellow"}
greenset={"bule","yellow"}
trivolor={"red","blue","yellow"}
if color1 not in trivolor or color2 not in trivolor or color1==color2:
    print("error")
elif s1==purpleset:
    print("purple")
elif s1==orangeset:
    print("orange")
else:
    print("green") 
