a=input()
b=input()
if a not in ["red","bule","yellow"]:
    print("error")
elif b not in ["red","bule","yellow"]:
    print("error")
elif a==b:
    print("error")
else:
    if a=="red" or b=="red":
        if a=="blue" or b=="blue":
            print("purple")
        else:
            print("orange")
    else:
        print("green")
