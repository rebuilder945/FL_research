a=input()
b=input()
ls1={"red","blue"}
ls2={"red","yellow"}
ls3={"blue","yellow"}
ls4={"red","blue","yellow"}
if a!=b and (a in ls4) and (b in ls4):
    if a in ls1 and b in ls1:
        print("purple")
    elif a in ls2 and b in ls2:
        print("orange")
    elif a in ls3 and b in ls3:
        print("green")
elif (a not in ls4) or (b not in ls4) or (a==b):
    print("error")
