color1=input()
color2=input()
s1={color1,color2}
purpleset={"red","blue"}
orangeset={"red","yellow"}
greenset={"blue","yellow"}
tricolor={"red","blue","yellow"}
if s1==purpleset:
    print("purple")
elif s1==orangeset:
    print("orange")
elif s1==greenset:
    print("green")
else:
    print("error")
