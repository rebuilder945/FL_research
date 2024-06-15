a=input()
b=input()
if a==b:
    print("error")
else:
    if a and b in ["red","blue"]:
        print("purplle")
    elif a and b in ["red","yellow"]:
        print("orange")
    elif a and b in ["blue","yellow"]:
        print("green")
    else:
        print("error")
