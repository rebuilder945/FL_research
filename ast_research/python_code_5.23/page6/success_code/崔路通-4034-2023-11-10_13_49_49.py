a=input()
b=input()
c=["red","blue","yellow"]
if a in c and b in c and a!=b:
    if a in c[0:2] and b in c[0:2]:
        print("purple")
    elif a in c[1:3] and b in c[1:3]:
        print("green")
    else:
        print("orange")
else:
    print("error")

