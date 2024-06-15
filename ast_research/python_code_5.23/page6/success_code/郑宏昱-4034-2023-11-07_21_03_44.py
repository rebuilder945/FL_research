a=input()
b=input()
lst=[a,b]
c=["red","blue","yellow"]
purple=["red","blue"]
orange=["red","yellow"]
green=["blue","yellow"]
if a not in c or b not in c or a==b:
    print("error")
else:
    if lst==purple:
        print("purple")
    if lst==green:
        print("green")
    if lst==orange:
        print("orange")
