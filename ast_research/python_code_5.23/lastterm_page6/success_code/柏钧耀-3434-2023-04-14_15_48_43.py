color=["blue","yellow","red"]
purple=["red","blue"]
green=["blue","yellow"]
orange=["red","yellow"]
a=input()
b=input()
if a not in color or b not in color:
    print("error")
elif a==b :
    print("error")
elif a in orange and b in orange:
    print("orange")
elif a in green and b in green:
    print("green")
elif a in purple and b in purple:
    print("purple")
else:
    print("error")
