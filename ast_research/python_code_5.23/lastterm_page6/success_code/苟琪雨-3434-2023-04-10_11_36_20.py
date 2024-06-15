a=input()
b=input()
if a =="red" and b=="yellow":
    print("orange")
elif a=="red" and b=="blue":
    print("purple")
elif a=="blue" and b=="red":
    print("purple")
elif a=="blue" and b=="yellow":
    print("green")
elif a=="yellow" and b=="red":
    print("orrange")
elif a=="yellow" and b=="blue":
    print("green")
else:
    print("error")
