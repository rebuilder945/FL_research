a=input()
b=input()
y=[a,b]
x=["red","blue","yellow"]
if a in x and b in x and a!=b:
    if "red" in y and "blue" in y:
        print("purple")
    elif "red" in y and "yellow" in y:
        print("orange")
    elif "yellow" in y and "blue" in y:
        print("green")
else:
    print("error")
