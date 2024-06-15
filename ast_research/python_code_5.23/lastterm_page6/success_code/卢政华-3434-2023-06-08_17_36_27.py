a=input()
b=input()
if (a=="red" and b=="blue" )or (b=="red" and a=="blue"):
    print("purple")
elif (a=="red" and b=="yellow") or(b=="red" and a=="yellow"):
    print("orange")
elif (a not in ("red", "blue", "yellow") or a == b):
    print("error")
else:
    print("green")
