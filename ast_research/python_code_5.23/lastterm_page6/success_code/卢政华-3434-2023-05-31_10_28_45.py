a=input()
b=input()
if a!="red" or "blue" or"yellow" and b !="red" or "blue" or"yellow":
    print("error")
if (a=="red" and b=="blue" )or (b=="red" and a=="blue"):
    print("purple")
elif (a=="red" and b=="yellow") or(b=="red" and a=="yellow"):
    print("orange")
else:
    print("green")
