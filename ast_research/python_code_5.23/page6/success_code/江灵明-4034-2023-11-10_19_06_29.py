a = input()
b = input()
if a==b:
    print("error")
if a and b in ["red","blue"]:
    print("purple")
if a and b in ["red","yellow"]:
    print("orange")
if a and b in ["blue","yellow"]:
    print("green")
else:
    print("error")
