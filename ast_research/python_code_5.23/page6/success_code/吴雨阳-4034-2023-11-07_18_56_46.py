a=input()

b=input()
sys={"red","yellow","blue"}
purpleset={"red","blue"}
orangeset={"red","yellow"}
greenset={"yellow","blue"}
color={a,b}
if color==purpleset:
    print("purple")
elif color==orangeset:
    print("orange")
elif color==greenset:
    print("green")
else:
    print("error")
