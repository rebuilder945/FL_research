a = input()
b = input()
list0 = ["red","yellow","blue"]
if a == b or a not in list0 or b not in list0:
    print("error")
if a == "red":
    if b == "yellow":
        print("orange")
    else:
        print("purple")
elif a == "yellow":
    if b == "red":
        print("orange")
    else:
        print("green")
elif a == "blue":
    if b == "red":
        print("purple")
    else:
        print("green")
