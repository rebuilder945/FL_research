a=input()
b=input()
s1={a,b}
purpleset={"red","blue"}
orangeset={"red","blue"}
greenset={"blue","yellow"}
triccolor={"red","blue","yellow"}
if s1 not in purpleset or s1 not in orangeset or s1 not in greenset or s1 not in triccolor:
    print("error")
elif s1==purpleset:
    print("purple")
elif s1==orangeset:
    print("orange")
elif s1==greenset:
    print("green")
