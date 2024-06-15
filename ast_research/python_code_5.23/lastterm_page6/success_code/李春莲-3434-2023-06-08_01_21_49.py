a=input()
b=input()
if (a=="red" and b=="blue") or (b=="red" and a=="blue"):
    print("purple")
elif (a=="red" and b=="yellow") or (b=="red" and a=="yellow"):
    print("orange")
elif (a=="blue" and b=="green") or (b=="blue" and a=="green"):
    print("green")
else:
    print("error")
