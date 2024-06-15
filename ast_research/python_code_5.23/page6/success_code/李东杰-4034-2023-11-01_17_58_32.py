a=input()
b=input()
s=["red","blue","yellow"]
if a not in s or b not in s or a==b:
    print("error")
else:
    if a in ["red","blue"] and b in ["red","blue"]:
        print("purple")
    elif a in ["red","yellow"] and b in ["red","yellow"]:
        print("orange")
    else:
        print('green')
    
