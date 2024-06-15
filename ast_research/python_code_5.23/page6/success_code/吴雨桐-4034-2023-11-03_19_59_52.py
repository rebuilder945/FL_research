co1=input()
co2=input()
if co1=="red":
    if co2=="blue":
        print("purple")
    elif co2=="yellow":
        print("orange")
    else:
        print("error")
elif co1=="blue":
    if co2=="red":
        print("purple")
    elif co2=="yellow":
        print("green")
    else:
        print("error")
elif co1=="yellow":
    if co2=="blue":
        print("green")
    elif co2=="red":
        print("orange")
    else:
        print("error")
else:
    print("error")
