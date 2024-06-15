purple=["red","blue"]
orange=["red","yellow"]
green=["blue","yellow"]
c1=input()
c2=input()
if c1==c2:
    print("error")
elif c1 in purple and c2 in purple:
    print("purple")
elif c1 in orange and c2 in orange:
    print("orange")
elif c1 in green and c2 in green:
    print("green")
else:
    print("error")
        
