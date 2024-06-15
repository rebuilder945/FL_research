a = input()
b = input()
if a == "red":
    if b == "blue":
        print("purple")
    if b == "yellow":
        print("orange")
elif a == "blue":
    if b == "red":
        print("purple")
    if b == "yellow":
        print("green")
elif a == "yellow":
    if b == "red":
        print("orange")
    if b == "blue":
        print("green")
else:
    print("error")
