a=input()
b=input()
s=["red","blue","yellow"]
if a not in s or a not in s or a==b:
    print("error")
elif a in ["red","blue"] and b in ["red","blue"]:
    print("purple")
elif a in ["red","yellow"] and b in ["red","yellow"]:
    print("orange")
elif a in ["blue","yellow"] and b in ["blue","yellow"]:
    print("green")
