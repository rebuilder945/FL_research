a = input()
b = input()
if a==b:
    print("error")
elif a and b in ["red","blue"]:
    print("purple")
elif a and b in ["red","yellow"]:
    print("orange")
elif a and b in ["blue","yellow"]:
    print("green")
else:
    print("error")
