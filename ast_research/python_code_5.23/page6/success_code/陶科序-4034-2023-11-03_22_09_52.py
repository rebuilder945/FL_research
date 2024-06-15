a = input()
b = input()
if a in ["red","blue","yellow"] and b in ["red","blue","yellow"] and a != b:
    if a == "red" and b == "blue":
        print("purple")
    if b == "red" and a == "blue":
        print("purple")
    if a == "red" and b == "yellow":
        print("orange")
    if b == "yellow" and a == "red":
        print("orange")
    if a == "yellow" and b == "blue":
        print("green")
    if b == "blue" and a == "yellow":
        print("green")
else:
    print("error")


