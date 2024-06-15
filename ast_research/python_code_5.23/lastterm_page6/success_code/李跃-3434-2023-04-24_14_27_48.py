a=input()
b=input()
if a=="red" and b=="blue":
    print("purple")
elif a=="red" and b=="yellow":
    print("orange")
elif a=="yellow" and b=="blue":
    print("green")
elif b=="red" and a=="blue":
    print("purple")
elif b=="red" and a=="yellow":
    print("orange")
elif b=="yellow" and a=="blue":
    print("green")
else:
    print("error")

