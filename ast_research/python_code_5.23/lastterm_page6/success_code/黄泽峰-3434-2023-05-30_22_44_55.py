a = input()
b = input()
pc = ["red","blue","yellow"]
if a == "red" and b =="blue":
    print("purple")
elif b == "red" and a =="blue":
    print("purple")
elif a == "red" and b == "yellow":
    print("orange")
elif b == "red" and a == "yellow":
    print("orange")
elif a == "blue" and b == "yellow":
    print("green")
elif b == "blue" and a == "yellow":
    print("green")
else:
    print("error")
