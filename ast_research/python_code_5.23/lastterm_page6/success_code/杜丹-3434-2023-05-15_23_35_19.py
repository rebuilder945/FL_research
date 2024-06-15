a=input()
b=input()
if (a=="red" and b=="blue") or (a=="blue" and b=="red"):
    print("purple")
elif (a=="red" and b=="yellow") or (a=="yellow" and b=="red"):
    print("orange")
elif (a=="yellow" and b=="blue") or(a=="blue" and b=="yellow"):
    print("green")
else:
    print("error")

