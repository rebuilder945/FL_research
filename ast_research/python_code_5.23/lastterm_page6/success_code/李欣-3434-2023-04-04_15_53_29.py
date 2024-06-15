c1=input()
c2=input()
ls=[c1,c2]
if "red" in ls:
    if "blue" in ls:
        print("purple")
    elif "yellow" in ls:
        print("orange")
    else:
        print("error")
elif "blue" in ls:
    if "yellow" in ls:
        print("green")
    else:
        print("error")
else:
    print("error")

