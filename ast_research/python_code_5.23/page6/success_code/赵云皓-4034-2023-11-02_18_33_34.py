a=input()
b=input()
c=["red","blue","yellow"]
d=["red","blue"]
e=["blue","yellow"]
if a in c and b in c and a!=b:
    if a in d and b in d:
        print("purple")
    elif a in e and b in e:
        print("green")
    else:
        print("orange")
else:
    print("error")
