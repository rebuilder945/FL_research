a=input(str())
b=input(str())
if a==b:
    print("error")
if (a!="red" and a!="blue" and a!="yellow") or (b!="red" and b!="blue" and b!="yellow"):
    print("error")
if (a=="red" and b=="blue") or (a=="blue" and b=="red"):
    print("purple")
if (a=="red" and b=="yellow") or (a=="yellow" and b=="red"):
    print("orange")
if (a=="blue" and b=="yellow") or (a=="yellow" and b=="blue"):
    print("green")
