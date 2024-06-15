a = input()
b = input()
c = {a,b}
purpleset={"red","blue","Red","Blue"}
orangeset={"red","yello","Red","Yello"}
greenset={"blue","yello","Blue","Yello"}
tricolor={"red","yello","blue","Red","Yello","Blue"}
if a not in tricolor or b not in tricolor or a==b:
    print("error")
elif c==purpleset:
    print("purple")
elif c==orangeset:
    print("orange")
else:
    print("green")

