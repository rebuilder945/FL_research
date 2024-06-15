color1=input().lower()
color2=input().lower()
S1={color1,color2}
purpleset={"red","blue"}
orangeset={"red","yellow"}
greenset={"blue","yellow"}
tricolor={"red","blue","yellow"}
if color1 not in tricolor or color2 not in tricolor or color1==color2:
    print("error")
elif S1==purpleset:
    print("purple")
elif S1==orangeset:
    print("orange")
else:
    print("green")
