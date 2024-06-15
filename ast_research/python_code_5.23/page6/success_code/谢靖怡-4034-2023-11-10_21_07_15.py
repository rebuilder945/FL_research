a=input()
b=input()
s1={a,b}
purpleset={"red","blue"}
orangeset={"red","blue"}
greenset={"blue","yellow"}
triccolor={"red","blue","yellow"}
if a not in triccolor or b not in triccolor or a==b:
    print("error")
elif s1==purpleset:
    print("purple")
elif s1==orangeset:
    print("orange")
elif s1==greenset:
    print("green")
